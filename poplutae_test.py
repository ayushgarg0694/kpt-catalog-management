from kpt_catalog_management.sql import base_class
from kpt_catalog_management.sql.models import Product, Category, Brand
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
import asyncio
from sqlalchemy import select, and_
import typing

async def anext(ait):
    return await ait.__anext__()

async def main():

    async with base_class.async_session() as session:
        async with session.begin():
            brand = "Aztec"
            category = "C2" 
            stmt = (
                select(Product, Brand, Category)
                .join(Brand, Product.brand_id == Brand.id)
                .join(Category, Product.category_id == Category.id)
                .where(and_(Brand.brand_name == brand, Category.name == category))
            )
            # product = await session.get(models.Product, 1,options = {
            #     "selectinload" : models.Category})
            
            result = await session.execute(stmt)
            ans = result.fetchall()
            #print(ans)
            for a in ans:
                print(a)
            #print(product.category)
            #result = await session.execute(select(models.Category).options(selectinload(models.Category.products)))
            # categories = result.scalars()
            # for c in categories:
            #     print(c)
            #     for p in c.products:
            #         print(p)
    

    # session: AsyncSession = await anext(base_class.get_session())
    # async with session.begin():
    #     categories: typing.List[models.Category] = await session.execute(select(models.Category))
    #     for c in categories:
    #         print(c)
    #         for p in c.products:
    #             print(p)

asyncio.run(main())

# p: models.Product = models.Product()