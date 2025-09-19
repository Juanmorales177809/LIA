from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.experiencia import (
    ExperienciaRead, ExperienciaCreate, ExperienciaUpdate
)
from app.crud import experiencia as crud

router = APIRouter(tags=["Experiencias"])


# Listar experiencias de una persona
@router.get("/personas/{id_persona}/experiencias", response_model=List[ExperienciaRead])
def list_experiencias(id_persona: int, db: Session = Depends(get_db)):
    experiencias = crud.get_all_by_persona(db, id_persona)
    return experiencias

# Crear experiencia para una persona
@router.post("/personas/{id_persona}/experiencias", response_model=ExperienciaRead, status_code=status.HTTP_201_CREATED)
def create_experiencia(id_persona: int, payload: ExperienciaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_for_persona(db, id_persona, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creando experiencia: {str(e)}")

# Obtener experiencia por ID
@router.get("/experiencias/{id_experiencia}", response_model=ExperienciaRead)
def get_experiencia(id_experiencia: int, db: Session = Depends(get_db)):
    obj = crud.get(db, id_experiencia)
    if not obj:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    return obj

# Actualizar experiencia
@router.put("/experiencias/{id_experiencia}", response_model=ExperienciaRead)
def update_experiencia(id_experiencia: int, payload: ExperienciaUpdate, db: Session = Depends(get_db)):
    obj = crud.update(db, id_experiencia, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    return obj

# Eliminar experiencia
@router.delete("/experiencias/{id_experiencia}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experiencia(id_experiencia: int, db: Session = Depends(get_db)):
    ok = crud.delete(db, id_experiencia)
    if not ok:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    return None
