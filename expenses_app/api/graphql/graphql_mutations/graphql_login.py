from ..imports import User
from graphql import GraphQLResolveInfo

class LoginInput:
    username: str
    password: str

    def get_mutation():
        return "Login(input: LoginInput): LoginResponse"
    
class LoginResponse:
    token: str
    error: str
    user: User