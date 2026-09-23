from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Kubernetes Incident Platform")


class Incident(BaseModel):
    name: str
    namespace: str
    resource: str
    resource_type: str
    reason: str

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

@app.post("/incidents")
def create_incident(incident: Incident):      

#     incident = Incident(
#     name="payment-api-crash",
#     namespace="dev",
#     reason="CrashLoopBackOff"
# )
    return {
        "incident": incident.name,
        "namespace": incident.namespace,
        "resource": incident.resource,
        "resource_type": incident.resource_type,
        "reason": incident.reason,
        "status": "received"
    }

                                                    