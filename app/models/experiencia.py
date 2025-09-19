from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Experiencia(Base):
    __tablename__ = "experiencia"
    __table_args__ = {"schema": "Personal"}  # ajusta el schema si lo tienes distinto

    idExperiencia = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPersona = Column(Integer, ForeignKey("Personal.personal.idPersona", ondelete="CASCADE"), nullable=False)

    cargo = Column(String(100), nullable=False)
    institucion = Column(String(150), nullable=False)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=True)

    # relación inversa hacia la persona
    persona = relationship("Personal", back_populates="experiencias")
