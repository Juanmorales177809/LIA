from typing import Optional
from datetime import date
from pydantic import BaseModel


# ----- Base -----
class ExperienciaBase(BaseModel):
    cargo: str
    institucion: str
    fechaInicio: date
    fechaFin: Optional[date] = None


# ----- Create -----
class ExperienciaCreate(ExperienciaBase):
    # idPersona se maneja en la ruta, no en el body
    pass


# ----- Update (parcial) -----
class ExperienciaUpdate(BaseModel):
    cargo: Optional[str] = None
    institucion: Optional[str] = None
    fechaInicio: Optional[date] = None
    fechaFin: Optional[date] = None


# ----- Read -----
class ExperienciaRead(ExperienciaBase):
    idExperiencia: int
    idPersona: int

    class Config:
        from_attributes = True   # ✅ Pydantic v2
