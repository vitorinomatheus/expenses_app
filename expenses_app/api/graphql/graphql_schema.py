from ariadne import gql, ObjectType, make_executable_schema
from .graphql_tools import *
from .imports import *
from flask import g
from .graphql_resolvers import GraphQLResolvers

class GraphQLSchema:

    def __init__(self, resolvers: GraphQLResolvers):
        self.type_query_schema = build_type_query(register_models + analysis_models)
        self.models_schema = convert_db_model_to_graphql_schema(register_models + analysis_models)
        self.additional_mutations = [LoginInput.get_mutation()]
        self.mutation = build_type_mutation(register_models, additional_mutations=self.additional_mutations)
        self.input_types = convert_model_to_graphql_input(register_models)

        self.type_defs = gql(f"""{self.type_query_schema}

        {self.models_schema}

        {self.mutation}

        {self.input_types}

        input LoginInput {{
            username: String!
            password: String!
        }}

        type LoginResponse {{
            token: String
            error: String
            user: User
        }}

        scalar Datetime""")

        self.resolvers = resolvers

        self.schema = make_executable_schema(self.type_defs, self.resolvers.query, self.resolvers.datetime_scalar, self.resolvers.mutation)
    
    def get_schema(self):
        return self.schema