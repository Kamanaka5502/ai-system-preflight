from fastapi import FastAPI
from preflight.engine import generate_preflight_spec

app = FastAPI()


@app.get("/preflight")
def preflight(idea: str):
    spec = generate_preflight_spec(idea)
    return {"preflight_spec": spec}

