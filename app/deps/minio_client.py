# deps/minio_client.py
from minio import Minio
import os

minio = Minio(
    os.getenv("MINIO_ENDPOINT", "192.168.88.248:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,  # True si usa HTTPS
)
