from models.products import Products
from sqlalchemy.orm import Session
from data_transfer_object import products


def get_product(id: int, db: Session):
    return db.query(products).filter(Products.id==id).first()


def create_product(data: products.Product, db: Session):
    product = Products(name=data.name)
    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except Exception as e:
        print(e)

    return product


def delete_product(id: int, db: Session):
    product = db.query().filter(products.id==id).delete()
    db.commit()
    return product


def update_product(data: products.Product, db: Session, id: int):
    product = db.query(Products).filter(Products.id==id).first()
    product.name = data.name
    product.description = data.description
    db.add(product)
    db.commit()
    db.refresh(product)

    return product
