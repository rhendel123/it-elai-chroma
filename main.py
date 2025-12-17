import chromadb
from chromadb.config import Settings

# Create Chroma client configured as a SERVER
chroma_client = chromadb.Client(
    Settings(
        chroma_api_impl="chromadb.api.fastapi.FastAPI",
        chroma_server_host="0.0.0.0",
        chroma_server_http_port=8000,
        allow_reset=True,
        anonymized_telemetry=False
    )
)

# Expose FastAPI app for Uvicorn
from chromadb.server.fastapi import app
