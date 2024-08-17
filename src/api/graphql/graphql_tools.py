def convert_table_to_schema(models: list) -> str:
    """
        The goal of this function is to get data from database tables
        and transform it into graphql schema

    """

def build_type_query(models: list) -> str:
    """
        The goal of this function is to build the base type for graphql schema
    """
    models_fields = [
        f"{model.__name__.lower()}(id: ID!): {model.__name__}"
        for model in models
    ]

    type_query = f"""
        type Query {{
            {"\n".join(models_fields)}
        }}
    """
    return type_query