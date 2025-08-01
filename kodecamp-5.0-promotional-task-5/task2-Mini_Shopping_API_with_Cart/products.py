from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

# Define actual products
product_list = [
    Product(id=1, name="Laptop", price=999.99),
    Product(id=2, name="Smartphone", price=499.49),
    Product(id=3, name="Headphones", price=79.99),
]
