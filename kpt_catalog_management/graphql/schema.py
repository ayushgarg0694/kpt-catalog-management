import typing
import strawberry
import datetime

@strawberry.type
class Brand:
    id: int
    name: str
    products: typing.List['Product']

@strawberry.type
class Category:
    id: int
    name: str
    owner_category: str
    category_code: int
    parent_id: int
    products: typing.List['Product']
    
@strawberry.type
class Product:
    id: int
    name: str
    category: 'Category'
    brand: 'Brand'
    pack_size: int
    product_type: str
    product_sub_type: str
    form: str
    prescription: str
    description: str
    manufacterer: str
    salt_composition: str
    images: typing.List['ProductImage']
    attributes: typing.List['ProductAttribute']
    pricing: typing.List['Pricing']

    

@strawberry.type
class ProductAttribute:
    id: int
    drug_info: str
    when_to_use: str
    how_to_use: str
    benefits: str
    side_effects: str
    product_id: int

@strawberry.type
class ProductImage:
    id: int
    product_id: int
    image: str

@strawberry.type
class Pricing:
    id: int
    price: float
    offer_price: float
    offer_start_date: datetime.datetime
    offer_end_date: datetime.datetime
    product_attribute: ProductAttribute



