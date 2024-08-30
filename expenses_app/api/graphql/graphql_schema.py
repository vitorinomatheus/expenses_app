from ariadne import gql, ObjectType, make_executable_schema
from .graphql_tools import build_type_query, convert_model_to_graphql_schema
from .imports import *
from flask import g
from .graphql_resolvers import GraphQLResolvers

models = [
    User,
    Expense,
    CatBudgetImpact,
    CatEmotional,
    CatExpenseFeel,
    CatExpenseType,
    CatSocial
]

type_query_schema = build_type_query(models)
models_schema = convert_model_to_graphql_schema(models)

type_defs = gql(f"""{type_query_schema}

{models_schema}""")

resolvers = GraphQLResolvers(models)

schema = make_executable_schema(type_defs, resolvers.query)