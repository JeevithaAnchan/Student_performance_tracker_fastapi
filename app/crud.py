from sqlalchemy.orm import Session
from app.models import Student
from app.schemas import StudentCreate
from app import schemas
from app.StudentFactory import StudentFactory
from app import models

# CREATE STUDENT
# Example create_student function
def create_student(db: Session, student: schemas.StudentCreate):
    if student.type == "graduate":
        db_student = models.GraduateStudent(
            name=student.name,
            department=student.department,
            type=student.type,
            thesis_title=student.thesis_title,
        )
    else:
        db_student = models.Student(
            name=student.name,
            department=student.department,
            type=student.type,
        )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# READ SINGLE STUDENT
def get_student(db: Session, student_id: str):
    return db.query(Student).filter(Student.student_id == student_id).first()

# READ MULTIPLE STUDENTS
def get_students(db: Session):
    return db.query(Student).all()

# UPDATE STUDENT
def update_student(db: Session, student_id: str, student_data: StudentCreate):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if not db_student:
        return None
    db_student.name = student_data.name
    db_student.department = student_data.department
    db_student.thesis_title = student_data.thesis_title
    db.commit()
    db.refresh(db_student)
    return db_student

# DELETE STUDENT
def delete_student(db: Session, student_id: str):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# SEARCH STUDENTS BY NAME
def find_students_by_name(db: Session, name: str):
    return db.query(Student).filter(Student.name.ilike(f"%{name}%")).all()
