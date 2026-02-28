from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Import our custom database tools and models
import models
from database import engine, get_db
from schemas import JobCreate, JobResponse

# 1. This line creates the actual tables in Postgres
# It looks at models.py and builds the table if it doesn't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Board with Postgres")

@app.get("/")
def home():
    return {"message": "Job Board is Connected to Postgres!"}

# CREATE: Add a job to the database
@app.post("/jobs/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    # Create a "Database Object" from our user input
    db_job = models.JobModel(
        title=job.title,
        company=job.company,
        location=job.location,
        salary=job.salary,
        is_remote=job.is_remote
    )
    db.add(db_job)        # Tell Postgres: "I want to add this"
    db.commit()          # Tell Postgres: "Save it permanently now"
    db.refresh(db_job)   # Get the new ID that Postgres generated
    return db_job

# READ: Get all jobs from the database
@app.get("/jobs/", response_model=List[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    # This is like writing "SELECT * FROM jobs" in SQL
    jobs = db.query(models.JobModel).all()
    return jobs