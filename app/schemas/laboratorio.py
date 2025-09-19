from pydantic import BaseModel
from typing import Optional


# ----- Base -----
class LaboratorioBase(BaseModel):
    nombre: str
    tipo: str
    ubicacion: Optional[str] = None
    idOnac: Optional[str] = None


# ----- Create -----
class LaboratorioCreate(LaboratorioBase):
    pass   # 👈 no lleva idLaboratorio, lo asigna la BD


# ----- Update (parcial) -----
class LaboratorioUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    ubicacion: Optional[str] = None
    idOnac: Optional[str] = None


# ----- Read (salida) -----
class LaboratorioOut(LaboratorioBase):
    idLaboratorio: int
    nombre: str

    class Config:
        from_attributes = True   # ✅ Pydantic v2
