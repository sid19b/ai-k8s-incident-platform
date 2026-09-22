from fastapi import FastAPI

app = FastAPI(title="AI Kubernetes Incident Platform")


@app.get("/")
def root():
    return {
        "service": "ai-service",
        "message": "AI Kubernetes Incident Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }