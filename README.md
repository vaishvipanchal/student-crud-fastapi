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

## doing commits

## commit 1

## API Testing

The API can be tested using the Swagger UI provided by FastAPI.

Open:

http://127.0.0.1:8000/docs

The following CRUD operations can be tested:

- Create a student using POST /students
- View all students using GET /students
- View a student by ID using GET /students/{student_id}
- Update a student using PUT /students/{student_id}
- Delete a student using DELETE /students/{student_id}
