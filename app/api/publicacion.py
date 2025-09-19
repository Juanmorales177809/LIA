from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas.publicacion import PublicacionOut, PublicacionCreate, PublicacionUpdate
from app.crud import publicacion as crud_publicacion

router = APIRouter(
    prefix="/personas/{id_persona}/publicaciones",
    tags=["Publicaciones"]
)

# Listar publicaciones de una persona
@router.get("/", response_model=List[PublicacionOut])
def list_publicaciones(id_persona: int, db: Session = Depends(get_db)):
    return crud_publicacion.get_all_by_persona(db, id_persona)

# Crear publicación para una persona
@router.post("/", response_model=PublicacionOut, status_code=status.HTTP_201_CREATED)
def create_publicacion(id_persona: int, payload: PublicacionCreate, db: Session = Depends(get_db)):
    return crud_publicacion.create_for_persona(db, id_persona, payload)

# CRUD por ID (no depende de persona, pero se mantiene accesible)
@router.get("/{id_pub}", response_model=PublicacionOut)
def get_publicacion(id_persona: int, id_pub: int, db: Session = Depends(get_db)):
    pub = crud_publicacion.get(db, id_pub)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return pub

@router.put("/{id_pub}", response_model=PublicacionOut)
def update_publicacion(id_persona: int, id_pub: int, payload: PublicacionUpdate, db: Session = Depends(get_db)):
    pub = crud_publicacion.update(db, id_pub, payload)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return pub

@router.delete("/{id_pub}", status_code=status.HTTP_204_NO_CONTENT)
def delete_publicacion(id_persona: int, id_pub: int, db: Session = Depends(get_db)):
    ok = crud_publicacion.delete(db, id_pub)
    if not ok:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return None
