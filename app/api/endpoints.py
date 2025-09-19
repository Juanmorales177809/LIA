from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db import get_db
from app.api.cargo import router as cargo_router
from app.api.laboratorio import router as laboratorio_router
from app.api.personal import router as personal_router
from app.api.formacion import router as formacion_router
from app.api.publicacion import router as publicacion_router
from app.api.experiencia import router as experiencia_router

api_router = APIRouter()

# Healthcheck de BD
@api_router.get("/ping-db")
def ping_database(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"conexion": "exitosa" if result == 1 else "fallida"}

# Montar routers de recursos
api_router.include_router(cargo_router, tags=["Cargos"])
api_router.include_router(laboratorio_router, tags=["Laboratorios"])
api_router.include_router(personal_router, tags=["Personal"])
api_router.include_router(formacion_router, tags=["Formación"])
api_router.include_router(publicacion_router, tags=["Publicaciones"])
api_router.include_router(experiencia_router, tags=["Experiencias"])

