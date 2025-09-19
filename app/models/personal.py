from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class Personal(Base):
    __tablename__ = "personal"
    __table_args__ = {"schema": "Personal"}

    idPersona = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    idCargo = Column(Integer, nullable=False)
    documento = Column(String(20), nullable=False)
    correo = Column(String(30), nullable=False)
    telefono = Column(String(20), nullable=False)
    estado = Column(Boolean, default=True)
    
    idCargo = Column(Integer, ForeignKey("Cargos.cargo.idCargo"), nullable=False)
    cargo = relationship("Cargo", back_populates="personal")
    
    
    formaciones = relationship(
        "Formacion",
        back_populates="persona",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    experiencias = relationship(
        "Experiencia",
        back_populates="persona",
        cascade="all, delete-orphan",
    )
    publicaciones = relationship(   # 👈 nombre consistente
        "AutorPublicacion",
        back_populates="persona",
        cascade="all, delete-orphan",
    )
