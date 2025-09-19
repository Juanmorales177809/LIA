from sqlalchemy.orm import Session 
from sqlalchemy import select
from app.models.cargo import Cargo
from app.models.laboratorio import Laboratorio
from app.models.personal import Personal
from app.schemas.personal import PersonalCreate, PersonalUpdate
from sqlalchemy.orm import Session, joinedload
from app.models.autorPublicacion import AutorPublicacion
from app.models.publicacion import Publicacion

def get_personal_all(db: Session):
    return db.query(Personal).all()

def get_personal_by_id(db: Session, id_persona: int):
    return db.query(Personal).filter(Personal.idPersona == id_persona).first()

def create_personal(db: Session, data: PersonalCreate):
    nuevo = Personal(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_personal(db: Session, id_persona: int, data: PersonalUpdate):
    persona = get_personal_by_id(db, id_persona)
    if not persona:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(persona, key, value)
    db.commit()
    db.refresh(persona)
    return persona

def delete_personal(db: Session, id_persona: int):
    persona = get_personal_by_id(db, id_persona)
    if persona:
        db.delete(persona)
        db.commit()
    return persona
def get_cv(db: Session, id_persona: int):
    persona = (
        db.query(Personal)
        .options(
            joinedload(Personal.formaciones),
            joinedload(Personal.experiencias),
            joinedload(Personal.publicaciones).joinedload(AutorPublicacion.publicacion)
        )
        .filter(Personal.idPersona == id_persona)
        .first()
    )
    return persona

def get_list_active(db: Session, skip: int = 0, limit: int = 100):
    rows = (
        db.query(
            Personal.idPersona.label("idPersona"),
            Personal.nombre.label("nombre"),
            Personal.estado.label("estado"),
            Cargo.nombre.label("cargo"),
            Laboratorio.nombre.label("laboratorio"),
        )
        .join(Cargo, Cargo.idCargo == Personal.idCargo)
        .outerjoin(Laboratorio, Laboratorio.idLaboratorio == Cargo.idLaboratorio)
        .filter(Personal.estado.is_(True))
        .order_by(Personal.nombre.asc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [
        {
            "idPersona": r.idPersona,
            "nombre": r.nombre,
            "estado": r.estado,
            "cargo": r.cargo,
            "laboratorio": r.laboratorio,
        }
        for r in rows
    ]


