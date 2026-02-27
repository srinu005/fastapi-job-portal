from pydantic import BaseModel, Field
from typing import Optional
class JobBase(BaseModel):
    title : str = Field(..., min_length = 3)
    company : str
    location : str
    salary : int = Field(..., gt=0)
    is_remote : bool = False

class JobCreate(JobBase):
    pass 

class JobResponse(JobBase):
    id : int