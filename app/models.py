import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    student_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    type = Column(String, nullable=False, default="normal")  # 'normal' or 'graduate'

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "normal",
        "with_polymorphic": "*"
    }

class GraduateStudent(Student):
    __tablename__ = "graduate_students"
    student_id = Column(String, ForeignKey("students.student_id"), primary_key=True)
    thesis_title = Column(String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "graduate"
    }