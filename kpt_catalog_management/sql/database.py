# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# import os
# from .base_class import Base


# DATABASE_URL = os.environ.get("DATABASE_URL")

# engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# #SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# # engine = create_engine(
# #     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# # )
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# async_session = sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False
# )

# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)

        
# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with async_session() as session:
#         yield session