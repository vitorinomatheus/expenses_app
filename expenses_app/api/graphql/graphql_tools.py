from ...constants import *
from ...infra.declarative_model_base import BaseModel
import inspect

def convert_db_model_to_graphql_schema(models: list[BaseModel]) -> str:
    """
        Get schema from database model and generate its GraphQL schema. \n
        For each model, the function will return a GraphQL type with mapped columns
    """
    schema_types = []

    for model in models:        
        type_props = [
            f"{SCHEMA_INDENT}{column.name}: {dbtype_to_graphqltype(column.type)}{"!" if column.nullable == "False" else ""}\n"
            for column in model.get_schema()
            if not column.only_mutation
        ]

        schema_type = f"type {model.__name__} {{{"\n".join(type_props)}}}"
        schema_types.append(schema_type)
    
    return f"{"\n\n".join(schema_types)}"

def build_type_query(models: list[BaseModel]) -> str:
    """
        Build the base type 'Query' for GraphQL schema from a list of models.\n
        The function returns the type Query which has a field for querying a single value for 
        each model as well as for querying a list of each model 
    """
    models_fields = []
    for model in models:
        single_query = f"{SCHEMA_INDENT}{model.__name__.lower()}(id: ID!): {model.__name__}"
        models_fields.append(single_query)
        
        if not getattr(model, 'ignore_list', False):
            list_query = f"{SCHEMA_INDENT}{model_to_list_name(model)}: [{model.__name__}!]"
            models_fields.append(list_query)

    type_query = f"""type Query {{
{"\n".join(models_fields)} \n}}\n"""
    
    return type_query

def convert_model_to_graphql_input(models: list[BaseModel]) -> str:
    """
        Build GraphQL input type for each model
    """
    inputs = []

    for model in models:        
        input_fields = [
            f"{SCHEMA_INDENT}{column.name}: {dbtype_to_graphqltype(column.type)}\n"
            for column in model.get_schema()
        ]

        input = f"input {model_to_input(model)} {{{"\n".join(input_fields)}}}"
        inputs.append(input)
    
    return f"{"\n\n".join(inputs)}"

def build_type_mutation(models: list[BaseModel], additional_mutations: list[str]) -> str:
    """
        Build the 'Mutation' type for GraphQL write operations
        The funcion returs the type Mutation which has a field for saving 
        as well as deleting each model
    """
    mutation_fields = [
        f"""{SCHEMA_INDENT}{model_to_save_field(model)}(id: ID, input: {model_to_input(model)}): {model.__name__}
{SCHEMA_INDENT}{model_to_delete_field(model)}(id: ID!): {model.__name__}!"""
        for model in models
    ]

    for mutation in additional_mutations:
        mutation_fields.append(f"{SCHEMA_INDENT}{mutation}")

    type_mutation = f"""type Mutation {{
{"\n".join(mutation_fields)} \n}}\n"""
    
    return type_mutation

def dbtype_to_graphqltype(type: str) -> str:
    """
        Convert the description of column's type generated from 
        database model's to GraphQL type's description pattern
    """
    if type == "integer":
        return "Int"
    elif type == "float":
        return "Float"
    elif type == "string":
        return "String"
    elif type == "boolean" or "bool":
        return "Boolean"
    elif type == "datetime":
        return "Datetime"
    
def get_type_name(attr_value):
    return dbtype_to_graphqltype(type(attr_value).__name__)

def model_to_list_name(model: BaseModel) -> str:
    return f"{model.__name__.lower()}{LIST_SCHEMA_SUFFIX}"

def model_to_save_field(model: BaseModel) -> str:
    return f"{MUTATION_SAVE_FIELD_PREFIX}{model.__name__}"

def model_to_delete_field(model: BaseModel) -> str:
    return f"{MUTATION_DELETE_FIELD_PREFIX}{model.__name__}"

def model_to_input(model: BaseModel) -> str:
    return f"Save{model.__name__}Input"