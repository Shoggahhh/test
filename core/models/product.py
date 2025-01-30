from sqlalchemy.orm import Mapped
from .base import Base


class Product(Base):
    article: Mapped[int]
    name: Mapped[int]
    price: Mapped[int]
    new_price: Mapped[int]
