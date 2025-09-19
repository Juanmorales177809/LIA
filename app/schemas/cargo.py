from pydantic import BaseModel
from typing import Optional


# -------- Base --------
class CargoBase(BaseModel):
    nombre: str
    idLaboratorio: Optional[int] = None


# -------- Create --------
class CargoCreate(CargoBase):
    pass


# -------- Update (parcial) --------
class CargoUpdate(BaseModel):
    nombre: Optional[str] = None
    idLaboratorio: Optional[int] = None


# -------- Read --------
class CargoOut(CargoBase):
    idCargo: int
    nombre: str

    class Config:
        from_attributes = True  # Pydantic v2
