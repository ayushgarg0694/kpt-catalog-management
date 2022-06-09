import sys
print(sys.path)
from kpt_catalog_management.config import Config
import typing as t

from sqlalchemy.ext.declarative import as_declarative, declared_attr

from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_async_engine(Config.DB_CONFIG, echo=True, future=True)

class_registry: t.Dict = {}

# Base = declarative_base()

@as_declarative(class_registry=class_registry)
class Base:
    id: t.Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        print(session)
        yield session