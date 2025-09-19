from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.db import Base

class AutorPublicacion(Base):
    __tablename__ = "autorPublicacion"
    __table_args__ = (
        PrimaryKeyConstraint("idPersona", "idPublicacion", name="pk_persona_publicacion"),
        {"schema": "Personal"},
    )

    idPersona = Column(Integer, ForeignKey("Personal.personal.idPersona"), nullable=False)
    idPublicacion = Column(Integer, ForeignKey("Personal.publicacion.idPublicacion"), nullable=False)

    # Relaciones
    persona = relationship("Personal", back_populates="publicaciones")
    publicacion = relationship("Publicacion", back_populates="autores_rel")
