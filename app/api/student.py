from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import StudentIn, StudentOut, StudentUpdate
from app.api import db_manager
from app.api.service import is_university_present

cloth = APIRouter()

@cloth.post('/', response_model=StudentIn, status_code=201)
async def create_student(payload: StudentIn):
    for student_id in payload.students_id:
        if not is_university_present(student_id):
            raise HTTPException(status_code=404, detail=f"student with given id:{student_id} not found")

    student_id = await db_manager.add_cloth(payload)
    response = {
        'id': student_id,
        **payload.dict()
    }

    return response

@cloth.get('/', response_model=List[StudentIn])
async def get_cloths():
    return await db_manager.get_all_cloths()

@cloth.get('/{id}/', response_model=StudentIn)
async def get_cloth(id: int):
    cloth = await db_manager.get_cloth(id)
    if not cloth:
        raise HTTPException(status_code=404, detail="Cloth not found")
    return cloth

@cloth.put('/{id}/', response_model=StudentIn)
async def update_cloth(id: int, payload: StudentUpdate):
    cloth = await db_manager.get_cloth(id)
    if not cloth:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = payload.dict(exclude_unset=True)

    if 'shops_id' in update_data:
        for shop_id in payload.shops_id:
            if not is_university_present(shop_id):
                raise HTTPException(status_code=404, detail=f"Shop with given id:{shop_id} not found")

    cloth_in_db = (StudentIn(**cloth))

    updated_cloth = cloth_in_db.copy(update=update_data)

    return await db_manager.update_cloth(id, updated_cloth)

@cloth.delete('/{id}/', response_model=None)
async def delete_student(id: int):
    student = await db_manager.get_cloth(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return await db_manager.delete_student(id)