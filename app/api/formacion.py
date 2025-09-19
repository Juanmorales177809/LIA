from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.schemas.formacion import FormacionOut, FormacionCreate, FormacionUpdate
from app.crud import formacion as crud_formacion

router = APIRouter(prefix="/personas/{id_persona}/formaciones", tags=["Formaciones"])

@router.get("/", response_model=List[FormacionOut])
def list_formaciones(id_persona: int, db: Session = Depends(get_db)):
    return crud_formacion.get_all_by_persona(db, id_persona)

@router.post("/", response_model=FormacionOut, status_code=status.HTTP_201_CREATED)
def create_formacion(id_persona: int, body: FormacionCreate, db: Session = Depends(get_db)):
    return crud_formacion.create_for_persona(db, id_persona, body)

@router.get("/{id_formacion}", response_model=FormacionOut)
def get_formacion(id_persona: int, id_formacion: int, db: Session = Depends(get_db)):
    obj = crud_formacion.get_by_id(db, id_formacion)
    if not obj or obj.idPersona != id_persona:
        raise HTTPException(status_code=404, detail="Formación no encontrada")
    return obj

@router.put("/{id_formacion}", response_model=FormacionOut)
def update_formacion(id_persona: int, id_formacion: int, updates: FormacionUpdate, db: Session = Depends(get_db)):
    obj = crud_formacion.get_by_id(db, id_formacion)
    if not obj or obj.idPersona != id_persona:
        raise HTTPException(status_code=404, detail="Formación no encontrada")
    return crud_formacion.update(db, obj, updates)

@router.delete("/{id_formacion}", status_code=status.HTTP_204_NO_CONTENT)
def delete_formacion(id_persona: int, id_formacion: int, db: Session = Depends(get_db)):
    obj = crud_formacion.get_by_id(db, id_formacion)
    if not obj or obj.idPersona != id_persona:
        raise HTTPException(status_code=404, detail="Formación no encontrada")
    crud_formacion.delete(db, obj)
    return None
