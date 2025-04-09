import src.script as sc

from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def home():
    """
    Function to check sent hello world
    """
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    """
    Function to check API health.
    """
    return {"status": "healthy"}


@app.get("/matching/score")
def get_matching_score():
    """
    Function to get matching score
    """
    num = sc.get_score()
    return num
