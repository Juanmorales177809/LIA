from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field


# ----- Base -----
class PublicacionBase(BaseModel):
    tipo: str
    titulo: str
    fecha: date
    revista: str
    doi: Optional[str] = None
    ISSN_ISBN: Optional[str] = None


# ----- Create -----
class PublicacionCreate(PublicacionBase):
    autores: List[int] = Field(default_factory=list)  # lista de idPersona


# ----- Update (parcial) -----
class PublicacionUpdate(BaseModel):
    tipo: Optional[str] = None
    titulo: Optional[str] = None
    fecha: Optional[date] = None
    revista: Optional[str] = None
    doi: Optional[str] = None
    ISSN_ISBN: Optional[str] = None
    autores: Optional[List[int]] = None


# ----- Read -----
class PublicacionOut(PublicacionBase):
    idPublicacion: int
    autores: List[int] = Field(default_factory=list)

    class Config:
        from_attributes = True   # ✅ Pydantic v2
