from ariadne import gql, ObjectType, make_executable_schema
from .graphql_tools import build_type_query, convert_model_to_graphql_schema
from .imports import *
from flask import g
from .graphql_resolvers import GraphQLResolvers

class GraphQLSchema:

    def __init__(self, resolvers: GraphQLResolvers):
        self.type_query_schema = build_type_query(models)
        self.models_schema = convert_model_to_graphql_schema(models)

        self.type_defs = gql(f"""{self.type_query_schema}

        {self.models_schema}""")

        self.resolvers = resolvers

        self.schema = make_executable_schema(self.type_defs, self.resolvers.query)
    
    def get_schema(self):
        return self.schema