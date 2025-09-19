from pydantic import BaseModel
from typing import Optional
from datetime import date


# ----- Base -----
class FormacionBase(BaseModel):
    nivel: str
    titulo: str
    institucion: str
    fechaFin: Optional[date] = None


# ----- Create -----
class FormacionCreate(FormacionBase):
    pass


# ----- Update (parcial) -----
class FormacionUpdate(BaseModel):
    nivel: Optional[str] = None
    titulo: Optional[str] = None
    institucion: Optional[str] = None
    fechaFin: Optional[date] = None


# ----- Read -----
class FormacionOut(FormacionBase):
    idFormacion: int
    idPersona: int

    class Config:
        from_attributes = True   # ✅ Pydantic v2
