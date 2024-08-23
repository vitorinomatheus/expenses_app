INDENT = "  "

def convert_table_to_schema(models: list) -> str:
    """
        The goal of this function is to get data from database tables
        and transform it into graphql schema
    """

    # column_info indexes: [0] = Name; [1] = Type; [2] = Nullable

    schema_types = []

    for model in models:
        
        type_props = ""

        for schema in model.get_schema():
            type_props += f"{INDENT}{schema[0]}: {dbtype_to_graphqltype(schema[1])}{"!" if schema[2] == "True" else ""}\n"

        schema_type = f"type {model.__name__} {{\n{type_props}}}"
        schema_types.append(schema_type)
    
    return f"{"\n\n".join(schema_types)}"


def build_type_query(models: list) -> str:
    """
        The goal of this function is to build the base type for graphql schema
    """
    models_fields = [
        f"""{INDENT}{model.__name__.lower()}(id: ID!): {model.__name__}
{INDENT}{model.__name__.lower()}_list: [{model.__name__}!]"""
        for model in models
    ]

    type_query = f"""type Query {{
{"\n".join(models_fields)} \n}}\n"""
    return type_query


def dbtype_to_graphqltype(type) -> str:
    """
        Tranform the type from database to graphql type
    """
    if type == "integer":
        return "Int"
    elif type == "float":
        return "Float"
    elif type == "string":
        return "String"
    elif type == "Boolean":
        return "Boolean"
