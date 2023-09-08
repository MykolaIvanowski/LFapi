from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db_connection import get_db_connection

from services import product_service
from data_transfer_object import products as product_dto

router = APIRouter()


@router.post(path='/', tags=["product"])
async def create(data: product_dto.Product = None, db: Session = Depends(get_db_connection)):
    return product_service.create_product(data, db)


@router.get(path='/{id}', tags=["product"])
async def get_user(id: str=None, db: Session = Depends(get_db_connection)):
    return product_service.get_product(id, db)


@router.delete(path='/{id}', tags=['product'])
async def delete_user(id: int = None, db: Session = Depends(get_db_connection)):
    return product_service.delete_product(id, db)


@router.put(path='/[id}', tags=['product'])
async def update_user(id: int =None, data: product_dto.Product = None, db: Session = Depends(get_db_connection)):
    return product_service.update_product(data, db, id)