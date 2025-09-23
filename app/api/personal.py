from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas.personal import PersonalCreate, PersonalUpdate, PersonalOut, PersonalBase, PersonalDetalleOut
from app.crud import personal as crud
from app.schemas.personal import PersonalListItem

# Prefijo y tag para Swagger
router = APIRouter(
    prefix="/personas",
    tags=["Personal"]
)

@router.get("/list", response_model=List[PersonalListItem])


def get_personal_list(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=500, description="Cantidad máxima de registros a devolver"),
    db: Session = Depends(get_db)
):
    personas = crud.get_list_active(db, skip=skip, limit=limit)
    return personas

@router.post("/", response_model=PersonalOut)
def create(data: PersonalCreate, db: Session = Depends(get_db)):
    return crud.create_personal(db, data)

@router.get("/", response_model=list[PersonalOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_personal_all(db)

@router.get("/{id_persona}", response_model=PersonalOut)
def read_one(id_persona: int, db: Session = Depends(get_db)):
    persona = crud.get_personal_by_id(db, id_persona)
    if not persona:
        raise HTTPException(status_code=404, detail="No encontrado")
    return persona

@router.put("/{id_persona}", response_model=PersonalOut)
def update(id_persona: int, data: PersonalUpdate, db: Session = Depends(get_db)):
    persona = crud.update_personal(db, id_persona, data)
    if not persona:
        raise HTTPException(status_code=404, detail="No encontrado")
    return persona

@router.delete("/{id_persona}")
def delete(id_persona: int, db: Session = Depends(get_db)):
    persona = crud.delete_personal(db, id_persona)
    if not persona:
        raise HTTPException(status_code=404, detail="No encontrado")
    return {"eliminado": True}

@router.get("/{id_persona}/cv")
def get_personal_cv(id_persona: int, db: Session = Depends(get_db)):
    persona = crud.get_cv(db, id_persona)
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

    pubs = [ap.publicacion for ap in persona.publicaciones]

    return {
        "idPersona": persona.idPersona,
        "nombre": persona.nombre,
        "documento": persona.documento,
        "correo": persona.correo,
        "telefono": persona.telefono,
        "estado": persona.estado,
        "formaciones": persona.formaciones,
        "experiencias": persona.experiencias,
        "publicaciones": pubs
    }

@router.get("/{id_persona}/detalle", response_model=PersonalDetalleOut)
def get_persona_detalle(id_persona: int, db: Session = Depends(get_db)):
    dto = crud.get_detalle(db, id_persona)
    if not dto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada")
    return dto