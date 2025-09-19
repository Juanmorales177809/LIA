from typing import Optional
from pydantic import BaseModel
from .laboratorio import LaboratorioOut
from .cargo import CargoOut

# -------- Base --------
class PersonalBase(BaseModel):
    nombre: str
    idCargo: int            # 👈 aquí está la clave, el cargo ya apunta al laboratorio
    documento: str
    correo: str
    telefono: Optional[str] = None
    estado: bool = True
    laboratorio: LaboratorioOut | None = None
    cargo: CargoOut | None = None
    
    class Config:
        from_attributes = True   # 👈 Pydantic v2

# -------- Create --------
class PersonalCreate(PersonalBase):
    pass    

# -------- Update --------
class PersonalUpdate(BaseModel):
    nombre: Optional[str] = None
    idCargo: Optional[int] = None
    documento: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[bool] = None

# -------- Read (salida) --------
class PersonalOut(PersonalBase):
    idPersona: int

    class Config:
        from_attributes = True   # 👈 Pydantic v2

class PersonalListItem(BaseModel):
    idPersona: int
    nombre: str
    estado: bool = True
    
    cargo: Optional[CargoOut] = None
    laboratorio: Optional[LaboratorioOut] = None

    class Config:
        from_attributes = True