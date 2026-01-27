from fastapi import FastAPI
import os
import socket
from datetime import datetime, timezone

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "API online",
        "hostname": socket.gethostname(),
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/info")
def info():
    return {
        "service": "api",
        "environment": os.getenv("ENVIRONMENT", "local"),
        "db": {
            "host": os.getenv("DB_HOST", "db"),
            "port": int(os.getenv("DB_PORT", "5432")),
            "name": os.getenv("DB_NAME", "app_db"),
            "user": os.getenv("DB_USER", "app_user"),
            "status": "not_connected",
        },
        "hostname": socket.gethostname(),
    }