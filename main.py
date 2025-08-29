from fastapi import FastAPI
from app.routers import students
from app.database import engine
from app.models import Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the students router
app.include_router(students.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Performance Tracker API"}