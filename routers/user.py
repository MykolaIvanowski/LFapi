from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db_connection import get_db_connection

from services import service as user_service
from data_transfer_object import user as user_dto

router = APIRouter()


@router.post(path='/', tags=["user"])
async def create(data: user_dto.User = None, db: Session = Depends(get_db_connection)):
    print("service post")
    return user_service.create_user(data, db)


@router.get(path='/{id}', tags=["user"])
async def get_user(id: str=None, db: Session = Depends(get_db_connection)):
    return user_service.get_user(id, db)
