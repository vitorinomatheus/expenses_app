from ariadne import ObjectType
from . imports import *
from .graphql_tools import model_to_list_name
from graphql import GraphQLResolveInfo

class GraphQLResolvers:
    def __init__(self, data_service: DataService):
        self.query = ObjectType("Query")
        self.set_type_query_base_resolvers()
        self.data_service = data_service
        self.mapped_models = self.map_types()

    def set_type_query_base_resolvers(self):
        for model in models:
            self.query.set_field(model.__name__.lower(), self.default_entity_query_resolver)
            self.query.set_field(model_to_list_name(model), self.default_list_query_resolver)

    def map_types(self):
        return { model.__name__.lower(): model for model in models }

    def default_entity_query_resolver(self, obj, info: GraphQLResolveInfo, id):
        type = self.get_field_type(info)
        data = self.data_service.get_entity(type, id)
        return data

    def default_list_query_resolver(self, obj, info):
        type = self.get_field_type(info)
        data = self.data_service.get_list(type)
        return data    
    
    def get_field_type(self, info: GraphQLResolveInfo) -> BaseModel:
        name = info.field_name

        if LIST_SCHEMA_SUFFIX in name:
            name = name.replace(LIST_SCHEMA_SUFFIX, "")
            
        return self.mapped_models.get(name)