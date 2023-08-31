from fastapi import FastAPI, HTTPException
import random
from typing import List

import structlog

from app.models import GenerateRandomArrayRequest, GenerateRandomArrayResponse

logger = structlog.getLogger(__name__)

app = FastAPI()


def generate_random_floats_array(dim: int) -> List[float]:
    """
    Generate a list of random floats.

    Args:
        dim (int): Dimension of the float array.

    Returns:
        List[float]: A list of random floats.
    """
    return [random.uniform(0, 1) for _ in range(dim)]


@app.post("/generate_random_array/", response_model=GenerateRandomArrayResponse)
def generate_random_array(request: GenerateRandomArrayRequest):
    """
    Generate a random float array for the given sentence.

    Args:
       request: request payload dictionary

    Returns:
        GenerateRandomArrayResponse: Response model with sentence and sentence vectors.
    """
    logger.info("Request received", sentence=request.sentence, dim=request.dim)

    if request.dim <= 0:
        logger.error("Invalid dimension", sentence=request.sentence, dim=request.dim)
        raise HTTPException(status_code=400, detail="Dimension must be a positive integer")

    try:
        floats_array = generate_random_floats_array(request.dim)
        logger.info("Array generated", sentence=request.sentence, dim=request.dim)
        return GenerateRandomArrayResponse(sentence=request.sentence, sent_vec=floats_array)
    except Exception as e:
        logger.exception("Error generating array", sentence=request.sentence, dim=request.dim, exception=str(e))
        raise HTTPException(status_code=500, detail=str(e))
