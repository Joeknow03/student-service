from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/students/openapi.json", docs_url="/api/v1/students/docs")

students_router = APIRouter()

students = [{'student_id': 1,
             'name': 'John Smith',
             'gender': 'Male',
             'age': 20,
             'learning': 'Computer Science',
             'city': 'New York'},
            {'student_id': 2,
             'name': 'Emma Johnson',
             'gender': 'Female',
             'age': 21,
             'learning': 'Biology',
             'city': 'Los Angeles'},
            {'student_id': 3,
             'name': 'Michael Lee',
             'gender': 'Male',
             'age': 19,
             'learning': 'History',
             'city': 'Chicago'},
            {'student_id': 4,
             'name': 'Sophia Garcia',
             'gender': 'Female',
             'age': 22,
             'learning': 'Psychology',
             'city': 'London'},
            {'student_id': 5,
             'name': 'Daniel Kim',
             'gender': 'Male',
             'age': 20,
             'learning': 'Engineering',
             'city': 'Tokyo'}]


@students_router.get("/")
async def read_students():
    return students


@students_router.get("/{students_id}")
async def read_students(students_id: int):
    for student in students:
        if student['students_id'] == students_id:
            return student
    return None


app.include_router(students_router, prefix='/api/v1/students', tags=['students'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
