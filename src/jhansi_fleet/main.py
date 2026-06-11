from fastapi import FastAPI

app = FastAPI(title="Jhansi Fleet")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
