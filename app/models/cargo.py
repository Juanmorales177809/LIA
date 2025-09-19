from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Cargo(Base):
    __tablename__ = "cargo"
    __table_args__ = {"schema": "Cargos"}

    idCargo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    idLaboratorio = Column(Integer, ForeignKey("Laboratorios.laboratorios.idLaboratorio"))

    laboratorio = relationship("Laboratorio", back_populates="cargo")
    personal = relationship("Personal", back_populates="cargo")
    

