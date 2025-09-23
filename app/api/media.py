# app/api/media.py
from fastapi import APIRouter, HTTPException
from datetime import timedelta
from minio import Minio
import os

router = APIRouter(prefix="/media", tags=["Media"])

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "192.168.88.248:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET    = os.getenv("MINIO_BUCKET", "imagenes")
MINIO_SECURE    = os.getenv("MINIO_SECURE", "false").lower() == "true"

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=MINIO_SECURE,
)

@router.get("/personal/{filename}")
def presign_personal_image(filename: str):
    """
    Espera que el objeto exista como:  bucket=imagenes, object_name=personal/{filename}
    Ej: GET /api/media/personal/3.jpg  -> personal/3.jpg
    """
    object_name = f"personal/{filename}"
    try:
        # 1) verifica existencia (si no existe, lanza)
        client.stat_object(MINIO_BUCKET, object_name)
    except Exception as e:
        # Log útil para ver la KEY exacta que está buscando
        print(f"[MINIO] NOT FOUND bucket={MINIO_BUCKET} object={object_name} err={e}")
        raise HTTPException(status_code=404, detail="Imagen no encontrada")

    # 2) genera URL firmada
    url = client.get_presigned_url(
        method="GET",
        bucket_name=MINIO_BUCKET,
        object_name=object_name,
        expires=timedelta(hours=1),
    )
    return {"url": url}
