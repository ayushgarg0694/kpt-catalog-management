from cgitb import text
from email.policy import default
from sqlalchemy import Column, Float, String, Integer, ForeignKey, null, Text, DateTime
# from sqlalchemy import String
# from sqlalchemy import Integer
from kpt_catalog_management.sql.base_class import Base
from sqlalchemy.orm import relationship, backref

class Category(Base):
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(100))
    owner_category = Column(String(100))
    category_code = Column(Integer, default=0)
    parent_id =  Column(Integer, ForeignKey('category.id'), index=True)
    parent  = relationship(lambda: Category, remote_side=id, backref='sub_category')
    products = relationship("Product", cascade="all, delete, delete-orphan" ,backref="category")
    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, name={self.name})>")
    
    def __str__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, name={self.name})>")

class Brand(Base):
    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(150))
    products = relationship("Product",   cascade="all, delete, delete-orphan", backref="brand")

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, name={self.brand_name})>")
    
    def __str__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, name={self.brand_name})>")


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer,ForeignKey('category.id'), index = True)
    brand_id = Column(Integer,ForeignKey('brand.id'), index = True)
    # category = relationship("Category", back_populates="products")
    # brand = relationship("Brand", back_populates="products")
    name = Column(String(100))
    pack_size = Column(Integer, default=0)
    product_type = Column(String(100), default = "", nullable=False)
    product_sub_type = Column(String(100), default="", nullable=False)
    form = Column(String(100), default = "", nullable=False)
    prescription = Column(String(50), default = "", nullable=False)
    pack_price = Column(Float(precision=5, decimal_return_scale=None))
    description = Column(Text)
    manufacturer = Column(String(150), default="", nullable = False)
    salt_composition = Column(String(200), default="", nullable = False)    
    images = relationship("ProductImage",cascade="all, delete, delete-orphan", backref="product")
    attributes = relationship("ProductAttribute",cascade="all, delete, delete-orphan",  backref="product" )
    pricing = relationship("Pricing",cascade="all, delete, delete-orphan",  backref="product" )
    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, name={self.name}, category={self.category_id}, brand = {self.brand_id})>")
    
    def __str__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, name={self.name}, category={self.category_id}, brand = {self.brand_id})>")

class ProductImage(Base):
    __tablename__="product_image"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'), index = True)
    image = Column(String(1000))

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id})>")
    
    def __str__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id})>")

class ProductAttribute(Base):
    __tablename__="product_attribute"
    id = Column(Integer, primary_key=True, index=True)
    drug_info = Column(Text)
    when_to_use = Column(String(200))
    how_to_use = Column(Text)
    benefits = Column(Text)
    side_effects = Column(Text)
    product_id = Column(Integer, ForeignKey('product.id'), index = True)

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id})>")
    
    def __str__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id})>")
class Pricing(Base):
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float(precision=5, decimal_return_scale=None))
    offer_price = Column(Float(precision=5, decimal_return_scale=None))
    offer_start_date = Column(DateTime)
    offer_end_date = Column(DateTime)
    product_attribute_id =  Column(Integer, ForeignKey('product_attribute.id'), index = True)
    product_id = Column(Integer, ForeignKey('product.id'), index = True)
    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}, price={self.price})>")
    
    def __str__(self) -> str:
        return (f"<{self.__class__.__name__}("
                f"id={self.id}>, price={self.price})")