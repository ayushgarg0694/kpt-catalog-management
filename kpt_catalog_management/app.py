from fastapi import FastAPI
import os

from strawberry.fastapi import GraphQLRouter
import strawberry

# stage = os.environ.get('STAGE', 'dev')


# app = FastAPI()

# @app.get("/")
# def index():
#     return {"Hello": "World"}


# @app.get("/users/{user_id}")
# def read_item(user_id: int):
#     return {"user_id": user_id}


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")