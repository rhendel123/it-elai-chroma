from fastapi import FastAPI
import chromadb

app = FastAPI()

client = chromadb.Client()

@app.get("/")
def root():
    return {"status": "Chroma is running"}
