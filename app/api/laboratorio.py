from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.laboratorio import LaboratorioCreate, LaboratorioUpdate, LaboratorioOut
from app.crud import laboratorio as crud

# Prefijo y tag para agrupar en Swagger
router = APIRouter(
    prefix="/laboratorios",
    tags=["Laboratorios"]
)

@router.post("/", response_model=LaboratorioOut)
def create(lab: LaboratorioCreate, db: Session = Depends(get_db)):
    return crud.create_laboratorio(db, lab)

@router.get("/", response_model=list[LaboratorioOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_laboratorios(db)

@router.get("/{id_lab}", response_model=LaboratorioOut)
def read_one(id_lab: str, db: Session = Depends(get_db)):
    lab = crud.get_laboratorio(db, id_lab)
    if not lab:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return lab

@router.put("/{id_lab}", response_model=LaboratorioOut)
def update(id_lab: str, lab_data: LaboratorioUpdate, db: Session = Depends(get_db)):
    lab = crud.update_laboratorio(db, id_lab, lab_data)
    if not lab:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return lab

@router.delete("/{id_lab}")
def delete(id_lab: str, db: Session = Depends(get_db)):
    lab = crud.delete_laboratorio(db, id_lab)
    if not lab:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return {"eliminado": True}
