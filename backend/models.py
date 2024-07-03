from pydantic import BaseModel, Field, PlainSerializer, AfterValidator, WithJsonSchema
from typing import Any, Optional, Annotated, Union

# Manejar identificadores de objetos en MongoDB
from bson import ObjectId


# Validar y convertir a ObjectID
def validate_object_id(v: Any) -> ObjectId:
    if isinstance(v, ObjectId):
        return v
    if ObjectId.is_valid(v):
        return ObjectId(v)
    raise ValueError("Invalid ObjectId")


#  Agregar metadatos y validadores personalizados
PyObjectId = Annotated[
    Union[str, ObjectId],
    AfterValidator(validate_object_id),
    PlainSerializer(lambda x: str(x), return_type=str),
    WithJsonSchema({"type": "string"}, mode="serialization"),
]


class Task(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        # Permitir que el modelo se cree a partir de atributos de una instancia
        from_attributes = True

        # Permitir que Pydantic use los alias de los campos al poblar el modelo
        populate_by_name = True

        # Indicarle a Pydantic que, al serializar un ObjectId,
        # debe convertirlo a una cadena
        json_encoders = {ObjectId: str}

        # Indicarle a Pydantic que permita el uso de ObjectId
        # como un tipo válido dentro del modelo Task
        arbitrary_types_allowed = True


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        from_attributes = True
        populate_by_name = True
