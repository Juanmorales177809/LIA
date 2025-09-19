from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.experiencia import Experiencia
from app.schemas.experiencia import ExperienciaCreate, ExperienciaUpdate

# Obtener una experiencia por ID
def get(db: Session, id_experiencia: int) -> Optional[Experiencia]:
    return db.query(Experiencia).filter(Experiencia.idExperiencia == id_experiencia).first()

# Listar todas las experiencias
def get_all(db: Session) -> List[Experiencia]:
    return db.query(Experiencia).all()

# Listar experiencias de una persona
def get_all_by_persona(db: Session, id_persona: int) -> List[Experiencia]:
    return db.query(Experiencia).filter(Experiencia.idPersona == id_persona).all()

# Crear experiencia ligada a una persona
def create_for_persona(db: Session, id_persona: int, payload: ExperienciaCreate) -> Experiencia:
    obj = Experiencia(
        idPersona=id_persona,
        cargo=payload.cargo,
        institucion=payload.institucion,
        fechaInicio=payload.fechaInicio,
        fechaFin=payload.fechaFin
    )
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception as e:
        db.rollback()
        raise e

# Actualizar experiencia existente
def update(db: Session, id_experiencia: int, payload: ExperienciaUpdate) -> Optional[Experiencia]:
    obj = get(db, id_experiencia)
    if not obj:
        return None
    
    try:
        for field, value in payload.dict(exclude_unset=True).items():
            setattr(obj, field, value)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception as e:
        db.rollback()
        raise e

# Actualizar fecha experiencia

# Eliminar experiencia
def delete(db: Session, id_experiencia: int) -> bool:
    obj = get(db, id_experiencia)
    if not obj:
        return False
    try:
        db.delete(obj)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
