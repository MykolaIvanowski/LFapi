from sqlalchemy import Boolean, Column, Integer, String
from db_connection import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=False, index=True)
    description = Column(String(255), unique=False, index=True)
    is_active = Column(Boolean, default=False)


class Vendors(Base):
    __tablename__ = 'vendors'

    vendor_id = Column(Integer,primary_key=True, index=True)
    vendor_name = Column(String(255), unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    address = Column(String(255), unique=False)