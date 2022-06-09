import base_class
import models
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio

async def main():
    session: AsyncSession = await base_class.get_session()

    categories = session.query(models.Category)

    for c in categories:
        print(c)

asyncio.run(main())