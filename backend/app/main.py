from fastapi import FastAPI

app = FastAPI(title="Review Dojo API")


@app.get("/")
def root():
    return {"message": "Review Dojo API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}