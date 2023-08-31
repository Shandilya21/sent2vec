from pydantic import BaseModel
from typing import List


class GenerateRandomArrayRequest(BaseModel):
    sentence: str
    dim: int = 500


class GenerateRandomArrayResponse(BaseModel):
    sentence: str
    sent_vec: List[float]
