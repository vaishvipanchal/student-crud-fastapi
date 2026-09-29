from fastapi import APIRouter, status
from typing import List

from models.student_model import Student, StudentCreate
from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter()


# 1. CREATE STUDENT
@router.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student_api(student: StudentCreate):
    return create_student(student)


# 2. READ ALL STUDENTS
@router.get(
    "/students",
    response_model=List[Student],
    status_code=status.HTTP_200_OK
)
def get_all_students_api():
    return get_all_students()


# 3. READ STUDENT BY ID
@router.get(
    "/students/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_student_api(student_id: int):
    return get_student_by_id(student_id)


# 4. UPDATE STUDENT
@router.put(
    "/students/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def update_student_api(
    student_id: int,
    student: StudentCreate
):
    return update_student(student_id, student)


# 5. DELETE STUDENT
@router.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student_api(student_id: int):
    delete_student(student_id)