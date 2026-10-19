from fastapi import FastAPI

app = FastAPI(
    title="Diabetes AI Support System",
    description="AI-assisted diabetes support system with Food and Glucometer Agents.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Diabetes AI Support System",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }