from sqlalchemy import Column, String, Boolean, Integer
from app.db import Base
from sqlalchemy.orm import relationship



class Laboratorio(Base):
    __tablename__ = "laboratorios"
    __table_args__ = {"schema": "Laboratorios"}

    idLaboratorio = Column(Integer, primary_key=True, index=True)  # Integer
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(10), nullable=False)
    ubicacion = Column(String(20), nullable=True)
    idOnac = Column(String(20), nullable=True)
    cargos = relationship("Cargo", back_populates="laboratorio")