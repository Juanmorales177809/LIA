# Dockerfile
FROM python:3.11-slim

# Evita buffering de logs
ENV PYTHONUNBUFFERED=1

# Instala dependencias del sistema (útiles para psycopg2 y similares)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Crea directorio de trabajo
WORKDIR /code

# Copia solo requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código (aunque en dev lo sobreescribiremos con volumen)
COPY . .

# Usa uvicorn en modo recarga
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
