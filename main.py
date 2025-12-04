from fastapi import FastAPI
from pydantic import BaseModel


class Sum(BaseModel):
    num1: float
    num2: float

app = FastAPI()

@app.post("/calculate")
async def get_sum(sum: Sum):
    return {"result" : sum.num1 + sum.num2}