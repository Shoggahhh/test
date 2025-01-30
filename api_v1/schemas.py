from pydantic import BaseModel


class ProductBase(BaseModel):
    article : str
    name : str
    price : str


class Product(ProductBase):
    id: int