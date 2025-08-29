from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    department: str

class StudentCreate(StudentBase):
    type: str
    thesis_title: Optional[str] = None

class StudentOut(StudentBase):
    student_id: str
    type: str
    thesis_title: Optional[str] = None

    class Config:
        from_attributes = True

class StudentResponse(StudentOut):
    class Config:
        from_attributes = True

class StudentListResponse(BaseModel):
    students: List[StudentResponse]