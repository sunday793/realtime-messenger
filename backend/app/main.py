from fastapi import FastAPI

app = FastAPI(title="Realtime Messenger")


@app.get("/health")
def health():
    return {"status":"ok"}