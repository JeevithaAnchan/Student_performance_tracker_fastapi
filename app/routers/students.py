from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Create student via factory inside CRUD
    return crud.create_student(db=db, student=student)

  
@router.get("/", response_model=schemas.StudentListResponse)
def read_students(db: Session = Depends(get_db)):
    students = crud.get_students(db)
    return {"students": students}
 
    

# -----------------------------
# Get a student by ID
# -----------------------------
@router.get("/{student_id}", response_model=schemas.StudentResponse)
def read_student(student_id: str, db: Session = Depends(get_db)):
    student = crud.get_student(db=db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# -----------------------------
# Update a student
# -----------------------------
@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: str, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db=db, student_id=student_id, student_data=student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

# -----------------------------
# Delete a student
# -----------------------------
@router.delete("/{student_id}", response_model=schemas.StudentResponse)
def delete_student(student_id: str, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db=db, student_id=student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student

# -----------------------------
# Search students by name (optional)
# -----------------------------
@router.get("/search/", response_model=List[schemas.StudentResponse])
def search_students(name: str, db: Session = Depends(get_db)):
    students = crud.find_students_by_name(db=db, name=name)
    if not students:
        raise HTTPException(status_code=404, detail=f"No students found with name '{name}'")
    
    return students

