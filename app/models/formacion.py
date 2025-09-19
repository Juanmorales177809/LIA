from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": "Personal"}

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(
        Integer,
        ForeignKey("Personal.personal.idPersona", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ← Mapeos a nombres REALES de la BD
    #   columna "nivelFormacion" -> atributo Python "nivel"
    nivel = Column("nivelFormacion", String(50), nullable=False, key="nivel")
    titulo = Column(String(100), nullable=False)         # en BD: varchar(100)
    institucion = Column(String(30), nullable=False)     # en BD: varchar(30)
    fechaFin = Column("fechaFinal", Date, nullable=True, key="fechaFin")

    # relación inversa
    persona = relationship("Personal", back_populates="formaciones")
