from fastapi import APIRouter
from conn.db import conn
from models.user import users
import strawberry
from type.user import Query, Mutation
from strawberry.asgi import GraphQL

user = APIRouter()
schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)
user.add_route('/graphql', graphql_app)

