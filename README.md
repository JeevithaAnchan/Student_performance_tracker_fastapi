# Student Performance Tracker API

## Overview
The Student Performance Tracker API is a RESTful API built using FastAPI that allows users to manage student records, including regular and graduate students. The API supports operations such as adding, removing, searching, and updating student information, as well as managing subject scores.

## Features
- Add regular and graduate students
- Remove students by ID
- Search for students by name
- Add subject scores for students
- List all students
- Retrieve the top scorer in a subject
- Calculate department average scores

## Technologies Used
- FastAPI: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- SQLite: A lightweight database for initial development, with potential to extend to PostgreSQL.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd student_performer_tracker_api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the API
To start the FastAPI application, run the following command:
```
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Endpoints
### Students
- **POST /students/**: Add a new student (regular or graduate).
- **DELETE /students/{student_id}**: Remove a student by ID.
- **GET /students/search**: Search for students by name.
- **POST /students/{student_id}/scores**: Add subject scores for a student.
- **GET /students/**: List all students.
- **GET /students/top-scorer**: Retrieve the top scorer in a subject.
- **GET /students/department-average**: Calculate the average score for a department.

## Example Usage
You can use tools like Postman or curl to interact with the API. Here are some example requests:

### Add a Regular Student
```
POST /students/
{
    "name": "John Doe",
    "department": "Computer Science"
}
```

### Search for a Student
```
GET /students/search?name=John
```

### Add Subject Scores
```
POST /students/S0001/scores
{
    "subject": "Mathematics",
    "marks": 95
}
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details."# Student_performance_tracker_fastapi" 
