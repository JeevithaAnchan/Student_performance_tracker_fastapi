from app.models import Student, GraduateStudent
from app.schemas import StudentCreate

class StudentFactory:
    @staticmethod
    def create(student: StudentCreate):
        if student.type == "graduate":
            return GraduateStudent(
                name=student.name,
                department=student.department,
                type=student.type,
                thesis_title=student.thesis_title,
            )
        else:
            return Student(
                name=student.name,
                department=student.department,
                type=student.type,
            )
