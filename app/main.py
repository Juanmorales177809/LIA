from fastapi import FastAPI
from app.api import endpoints, laboratorio, personal, cargo, formacion, publicacion, experiencia
from fastapi.middleware.cors import CORSMiddleware
import os

origins = [os.getenv("FRONTEND_ORIGIN")]
app = FastAPI()

app.include_router(laboratorio.router, prefix="/api") 
app.include_router(personal.router, prefix="/api")
app.include_router(cargo.router, prefix="/api")
app.include_router(formacion.router, prefix="/api")
app.include_router(publicacion.router, prefix="/api")
app.include_router(experiencia.router, prefix="/api")
# app.include_router(responsabilidades.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
