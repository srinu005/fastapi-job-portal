from fastapi import FastAPI, HTTPException
from typing import List
from schemas import JobCreate, JobResponse

app = FastAPI( title ='Job Board API')

#Temporary Database

jobs_db = []
id_counter = 1
@app.get("/")
async def home():
    return {"message": "JOB Board is Online"}

@app.post("/jobs/", response_model = JobResponse)
async def create_job( job: JobCreate):
    global id_counter
    new_job = job.model_dump()
    new_job["id"] = id_counter
    jobs_db.append(new_job)
    id_counter += 1
    return new_job

@app.get("/jobs/", response_model = List[JobResponse])
async def get_jobs():
    return jobs_db

