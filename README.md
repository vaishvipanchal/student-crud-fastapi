# FastAPI Student CRUD Application

## Description

This project is a simple REST API built using FastAPI for managing university student records.

The application provides CRUD operations for student data and stores the data using local in-memory storage.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Student Fields

Each student contains:

- ID
- Name
- Email
- Course
- Semester

## API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/students`      | Create a student  |
| GET    | `/students`      | Get all students  |
| GET    | `/students/{id}` | Get student by ID |
| PUT    | `/students/{id}` | Update student    |
| DELETE | `/students/{id}` | Delete student    |

## Project Structure

```text
student-crud/
├── main.py
├── requirements.txt
├── models/
│   └── student_model.py
├── routes/
│   └── student_routes.py
└── controllers/
    └── student_controller.py
```
