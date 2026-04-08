from fastapi import FastAPI

app = FastAPI(title="n8n_test_fastapi_v2")

@app.get("/health")
def health():
    return {"status": "ok", "service": "n8n_test_fastapi_v2"}

