from sqlalchemy.orm import Session
from app.models.formacion import Formacion
from app.schemas.formacion import FormacionCreate, FormacionUpdate

def get_all_by_persona(db: Session, id_persona: int):
    return db.query(Formacion).filter(Formacion.idPersona == id_persona).all()

def get_by_id(db: Session, id_formacion: int) -> Formacion | None:
    return db.query(Formacion).filter(Formacion.idFormacion == id_formacion).first()

def create_for_persona(db: Session, id_persona: int, body: FormacionCreate):
    obj = Formacion(idPersona=id_persona, **body.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, db_obj: Formacion, updates: FormacionUpdate):
    for k, v in updates.model_dump(exclude_unset=True).items():
        setattr(db_obj, k, v)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, db_obj: Formacion):
    db.delete(db_obj)
    db.commit()
