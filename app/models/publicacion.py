from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from app.db import Base

class Publicacion(Base):
    __tablename__ = "publicacion"
    __table_args__ = {"schema": "Personal"}  # 👈 corregido

    idPublicacion = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(30), nullable=False)
    titulo = Column(String(100), nullable=False)
    fecha = Column(Date, nullable=False)
    revista = Column(String(50), nullable=False)
    doi = Column(String(100), nullable=True)
    ISSN_ISBN = Column(String(50), nullable=True)

    # Relación con autores
    autores_rel = relationship(
        "AutorPublicacion",
        back_populates="publicacion",
        cascade="all, delete-orphan"
    )
