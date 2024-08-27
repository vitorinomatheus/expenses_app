from ariadne import gql, ObjectType, make_executable_schema
from .graphql_tools import build_type_query, convert_model_to_graphql_schema
from .imports import *
from flask import g

models = [
    User,
    Expense,
    CatBudgetImpact,
    CatEmotional,
    CatExpenseFeel,
    CatExpenseType,
    CatSocial
]

type_defs = gql(f"""{build_type_query(models)}

{convert_model_to_graphql_schema(models)}""")

query = ObjectType("Query")
user = ObjectType("User")


@query.field("user")
def resolve_user(_, info, id):
    teste = g.db.query(User)
    return teste

# @user.field("email")
# def resolve_username(obj, *_):
#     print("Resolver hit")

schema = make_executable_schema(type_defs, user, query)