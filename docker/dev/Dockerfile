# Usa l'immagine base Python 3.9
FROM python:3.9

# Imposta il working directory all'interno del container
WORKDIR /app

# Installa Poetry
RUN pip install poetry

RUN pip install uvicorn

# Copia i file di configurazione di Poetry (pyproject.toml e poetry.lock) nella directory /app
COPY pyproject.toml /app/

# Installa le dipendenze del progetto utilizzando Poetry
RUN poetry install

# Copia il codice sorgente nella directory /app
COPY .. /app

# Esponi la porta 8000 per FastAPI
EXPOSE 8000

# Comando per avviare il server FastAPI
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--reload"]

