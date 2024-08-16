from ariadne import gql, QueryType, make_executable_schema

type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()

schema = make_executable_schema(type_defs, query)

# root resolver (discarding the first argument)
@query.field("hello")
def resolver_hello(_,  info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent