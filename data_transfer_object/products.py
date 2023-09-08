from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    description: str


class Vendors(BaseModel):
    vendor_name: str
    product_id: Optional
    address: str
