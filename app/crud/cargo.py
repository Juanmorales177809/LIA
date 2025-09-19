from sqlalchemy.orm import Session
from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreate, CargoUpdate


def get_all(db: Session):
    """Obtener todos los cargos"""
    return db.query(Cargo).all()


def get_by_id(db: Session, id_cargo: int):
    """Obtener un cargo por ID"""
    return db.query(Cargo).filter(Cargo.idCargo == id_cargo).first()


def create(db: Session, cargo: CargoCreate):
    """Crear un nuevo cargo"""
    db_cargo = Cargo(**cargo.dict())
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo


def update(db: Session, db_obj: Cargo, updates: CargoUpdate):
    """Actualizar un cargo existente"""
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete(db: Session, db_obj: Cargo):
    """Eliminar un cargo"""
    db.delete(db_obj)
    db.commit()
    return db_obj
