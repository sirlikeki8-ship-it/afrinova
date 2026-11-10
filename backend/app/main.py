from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AfriNova API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "afrinova-api"}

@app.get("/api/v1/ping")
def ping():
    return {"success": True, "data": {"message": "AfriNova backend is alive"}}
