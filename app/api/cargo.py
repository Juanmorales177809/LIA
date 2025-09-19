from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.cargo import CargoCreate, CargoUpdate, CargoOut
from app.crud import cargo as crud_cargo
from app.db import get_db

# Prefijo y tag para agrupar en Swagger
router = APIRouter(
    prefix="/cargos",
    tags=["Cargos"]
)

@router.post("/", response_model=CargoOut, status_code=201)
def create_cargo(cargo: CargoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo cargo"""
    return crud_cargo.create(db, cargo)


@router.get("/", response_model=List[CargoOut])
def read_cargos(db: Session = Depends(get_db)):
    """Obtener todos los cargos"""
    return crud_cargo.get_all(db)


@router.get("/{id_cargo}", response_model=CargoOut)
def read_cargo(id_cargo: int, db: Session = Depends(get_db)):
    """Obtener un cargo por ID"""
    db_cargo = crud_cargo.get_by_id(db, id_cargo)
    if not db_cargo:
        raise HTTPException(status_code=404, detail="Cargo no encontrado")
    return db_cargo


@router.put("/{id_cargo}", response_model=CargoOut)
def update_cargo(id_cargo: int, cargo: CargoUpdate, db: Session = Depends(get_db)):
    """Actualizar un cargo existente"""
    db_cargo = crud_cargo.get_by_id(db, id_cargo)
    if not db_cargo:
        raise HTTPException(status_code=404, detail="Cargo no encontrado")
    return crud_cargo.update(db, db_cargo, cargo)


@router.delete("/{id_cargo}", status_code=204)
def delete_cargo(id_cargo: int, db: Session = Depends(get_db)):
    """Eliminar un cargo"""
    db_cargo = crud_cargo.get_by_id(db, id_cargo)
    if not db_cargo:
        raise HTTPException(status_code=404, detail="Cargo no encontrado")
    crud_cargo.delete(db, db_cargo)
    return {"ok": True}
