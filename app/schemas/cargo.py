from pydantic import BaseModel
from typing import Optional


# -------- Base --------
class CargoBase(BaseModel):
    nombreCargo: str
    idLaboratorio: Optional[int] = None


# -------- Create --------
class CargoCreate(CargoBase):
    pass
    


# -------- Update (parcial) --------
class CargoUpdate(BaseModel):
    nombre: Optional[str] = None
    idLaboratorio: Optional[int] = None



# ------- Read con laboratorio anidado --------
class LaboratorioOut(BaseModel):
    idLaboratorio: int
    nombre: str

    class Config:
        from_attributes = True  # Pydantic v2 (antes orm_mode = True)

class CargoOut(BaseModel):
    idCargo: int
    nombreCargo: str
    laboratorio: Optional[LaboratorioOut]  # 👈 relación anidada

    class Config:
        from_attributes = True