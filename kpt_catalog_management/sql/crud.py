categfrom sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
import asyncio
from sqlalchemy import select
from sqlalchemy import and_
from kpt_catalog_management.sql.models import Category, Brand, Product


async def get_products(
    session: AsyncSession, product_id=None, brand=None, category=None
):

    stmt = select(Product)

    if product_id:
        stmt = stmt.where("id" == product_id)
    else:

        if brand and category:
            stmt = (
                select(Product, Brand, Category)
                .join(Brand, Product.brand_id == Brand.id)
                .join(Category, Product.category_id == Category.id)
                .where(and_(Brand.name == brand, Category.name == category))
            )
