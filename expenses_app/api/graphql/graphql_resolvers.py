from ariadne import ObjectType
from . imports import *
from .graphql_tools import model_to_list_name

class GraphQLResolvers:
    def __init__(self, models: list[BaseModel]):
        self.query = ObjectType("Query")
        self.models = models
        self.set_type_query_base_resolvers()

    def set_type_query_base_resolvers(self):
        for model in self.models:
            self.query.set_field(model.__name__.lower(), self.default_entity_query_resolver)
            self.query.set_field(model_to_list_name(model), self.default_list_query_resolver)


    def default_entity_query_resolver(self, obj, info, id):
        pass

    def default_list_query_resolver(self, obj, info):
        pass