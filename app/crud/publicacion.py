from sqlalchemy.orm import Session
from app.models.publicacion import Publicacion
from app.models.autorPublicacion import AutorPublicacion
from app.schemas.publicacion import PublicacionCreate, PublicacionUpdate


# ---- CRUD plano ----
def get_all(db: Session):
    return db.query(Publicacion).all()


def get(db: Session, id_pub: int):
    return db.query(Publicacion).filter(Publicacion.idPublicacion == id_pub).first()


def create(db: Session, payload: PublicacionCreate):
    nueva = Publicacion(**payload.dict(exclude={"autores"}))
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    # Relacionar autores si se pasan
    if payload.autores:
        for id_persona in payload.autores:
            autor = AutorPublicacion(idPersona=id_persona, idPublicacion=nueva.idPublicacion)
            db.add(autor)
        db.commit()

    return nueva


def update(db: Session, id_pub: int, payload: PublicacionUpdate):
    pub = get(db, id_pub)
    if not pub:
        return None

    # Actualizar atributos simples
    for key, value in payload.dict(exclude_unset=True, exclude={"autores"}).items():
        setattr(pub, key, value)

    db.commit()
    db.refresh(pub)

    # Actualizar autores si llegan
    if payload.autores is not None:
        db.query(AutorPublicacion).filter_by(idPublicacion=id_pub).delete()
        for id_persona in payload.autores:
            autor = AutorPublicacion(idPersona=id_persona, idPublicacion=id_pub)
            db.add(autor)
        db.commit()

    return pub


def delete(db: Session, id_pub: int):
    pub = get(db, id_pub)
    if not pub:
        return False
    db.delete(pub)
    db.commit()
    return True


# ---- Métodos anidados ----
def get_all_by_persona(db: Session, id_persona: int):
    return (
        db.query(Publicacion)
        .join(AutorPublicacion)
        .filter(AutorPublicacion.idPersona == id_persona)
        .all()
    )


def create_for_persona(db: Session, id_persona: int, payload: PublicacionCreate):
    # Crear publicación
    nueva = Publicacion(**payload.dict(exclude={"autores"}))
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    # Relacionar automáticamente con el id_persona de la ruta
    autor = AutorPublicacion(idPersona=id_persona, idPublicacion=nueva.idPublicacion)
    db.add(autor)

    # Si hay más autores, añadirlos también
    if payload.autores:
        for otro in payload.autores:
            if otro != id_persona:  # evitar duplicar
                autor_extra = AutorPublicacion(idPersona=otro, idPublicacion=nueva.idPublicacion)
                db.add(autor_extra)

    db.commit()
    return nueva
