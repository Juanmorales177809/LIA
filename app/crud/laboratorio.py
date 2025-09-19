from sqlalchemy.orm import Session
from app.models.laboratorio import Laboratorio
from app.schemas.laboratorio import LaboratorioCreate, LaboratorioUpdate

def get_laboratorios(db: Session):
    return db.query(Laboratorio).all()

def get_laboratorio(db: Session, id_lab: str):
    return db.query(Laboratorio).filter(Laboratorio.idLaboratorio == id_lab).first()

def create_laboratorio(db: Session, lab: LaboratorioCreate):
    nuevo = Laboratorio(**lab.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_laboratorio(db: Session, id_lab: str, lab_data: LaboratorioUpdate):
    lab = get_laboratorio(db, id_lab)
    if not lab:
        return None
    for field, value in lab_data.dict(exclude_unset=True).items():
        setattr(lab, field, value)
    db.commit()
    db.refresh(lab)
    return lab

def delete_laboratorio(db: Session, id_lab: str):
    lab = get_laboratorio(db, id_lab)
    if lab:
        db.delete(lab)
        db.commit()
    return lab
