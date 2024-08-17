from ariadne import gql, QueryType, make_executable_schema
from .graphql_tools import build_type_query, convert_table_to_schema

type_defs = gql(f"""
    {build_type_query()}

    {convert_table_to_schema()}
""")

query = QueryType()

schema = make_executable_schema(type_defs, query)

# root resolver (discarding the first argument)
@query.field("hello")
def resolver_hello(_,  info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent