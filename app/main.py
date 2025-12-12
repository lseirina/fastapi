from fastapi import FastAPI
import logging

logging.BaseConfig(level=logging.INFO)
logger = logging.getlogger(__name__)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/custom")
def read_custom():
    logger.info("Handling request to root endpoint")
    return {"This is a custom message"}