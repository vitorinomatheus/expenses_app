from ariadne import ObjectType, MutationType, ScalarType
from . imports import *
from .graphql_tools import *
from graphql import GraphQLResolveInfo
from datetime import datetime

class GraphQLResolvers:
    def __init__(self, data_service: DataService, auth_wall: AuthWall):
        self.query = ObjectType("Query")
        self.mutation = MutationType()
        self.datetime_scalar = ScalarType("Datetime")
        self.datetime_scalar.set_serializer(lambda value: value.isoformat())
        self.datetime_scalar.set_value_parser(lambda value: datetime.fromisoformat(value))
        self.set_base_resolvers()
        self.data_service = data_service
        self.auth_wall = auth_wall
        self.mapped_models = self.map_types()

    def default_entity_query_resolver(self, _, info: GraphQLResolveInfo, id):
        type = self.get_field_type(info)
        auth_token = info.context['request'].authorization.token
        return self.auth_wall.authorize(
            token=auth_token,
            method=self.data_service.get_entity,
            model=type,
            id=id
        )

    def default_list_query_resolver(self, _, info):
        type = self.get_field_type(info)
        auth_token = info.context['request'].authorization.token
        return self.auth_wall.authorize(auth_token, self.data_service.get_list, model=type)

    def default_save_resolver(self, _, info: GraphQLResolveInfo, **kwargs):
        id = kwargs.get('id')
        data = kwargs.get('input')
        type = self.get_field_type(info)
        auth_token = info.context['request'].authorization.token
        for key, value in data.items():
            setattr(type, key, value)
        if id:
            type.id = id

        return self.auth_wall.authorize(auth_token, self.data_service.save_entity, model=type)

    def default_delete_resolver(self, _, info: GraphQLResolveInfo, id):
        type = self.get_field_type(info)
        auth_token = info.context['request'].authorization.token
        return self.auth_wall.authorize(
            auth_token, 
            self.data_service.delete_entity, 
            model=type, 
            id=id
        )
    
    def set_base_resolvers(self):
        for model in register_models:
            self.query.set_field(model.__name__.lower(), self.default_entity_query_resolver)
            self.query.set_field(model_to_list_name(model), self.default_list_query_resolver)
            self.mutation.set_field(model_to_save_field(model), self.default_save_resolver)
            self.mutation.set_field(model_to_delete_field(model), self.default_delete_resolver)
        for model in analysis_models:
            self.query.set_field(model.__name__.lower(), self.default_entity_query_resolver)
        self.mutation.set_field('Login', self.login_resolver)

    def login_resolver(self, _, info: GraphQLResolveInfo, input):
        login_service = LoginService()
        return login_service.login(input)
    
    def map_types(self):
        return { model.__name__.lower(): model for model in register_models }
    
    def get_field_type(self, info: GraphQLResolveInfo) -> BaseModel:
        name = info.field_name

        if LIST_SCHEMA_SUFFIX in name:
            name = name.replace(LIST_SCHEMA_SUFFIX, "")

        if MUTATION_DELETE_FIELD_PREFIX in name:
            name = name.replace(MUTATION_DELETE_FIELD_PREFIX, "").lower()

        if MUTATION_SAVE_FIELD_PREFIX in name:
            name = name.replace(MUTATION_SAVE_FIELD_PREFIX, "").lower()
            
        model = self.mapped_models.get(name)
        return model()   