from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: load corpus and train NGramModel at startup

class ScoreReq(BaseModel):
    password: str

@app.post("/score")
def score(req: ScoreReq):
    # TODO: return real scoring
    return {"score": 0, "category": "TODO", "reasons": ["stub"], "entropyBits": 0.0}

@app.get("/generate")
def generate(mode: str = "secure", length: int = 12, temp: float = 0.9):
    # TODO: branch secure vs learned
    return {"password": "PLACEHOLDER", "reasons": ["stub"]}
