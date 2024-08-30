from ...constants import *
from ...infra.declarative_model_base import BaseModel

def convert_model_to_graphql_schema(models: list[BaseModel]) -> str:
    """
        Get schema from database model and generate its GraphQL schema. \n
        For each model, the function will return a GraphQL type with mapped columns
    """
    schema_types = []

    for model in models:        
        type_props = [
            f"{SCHEMA_INDENT}{column.name}: {dbtype_to_graphqltype(column.type)}{"!" if column.nullable == "True" else ""}\n"
            for column in model.get_schema()
        ]

        schema_type = f"type {model.__name__} {{{"\n".join(type_props)}}}"
        schema_types.append(schema_type)
    
    return f"{"\n\n".join(schema_types)}"


def build_type_query(models: list[BaseModel]) -> str:
    """
        Build the base type 'Query' for GrapQL schema from a list of models.\n
        The function returns the type Query which has a field for querying a single value for 
        each model as well as for querying a list of each model 
    """
    models_fields = [
        f"""{SCHEMA_INDENT}{model.__name__.lower()}(id: ID!): {model.__name__}
{SCHEMA_INDENT}{model_to_list_name(model)}: [{model.__name__}!]"""
        for model in models
    ]

    type_query = f"""type Query {{
{"\n".join(models_fields)} \n}}\n"""
    
    return type_query


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
    elif type == "boolean":
        return "Boolean"

def model_to_list_name(model: BaseModel):
    return f"{model.__name__.lower()}{LIST_SCHEMA_SUFFIX}"