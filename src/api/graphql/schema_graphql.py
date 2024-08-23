from imports import *

models = [
    User,
    Expense,
    CatBudgetImpact,
    CatEmotional,
    CatExpenseFeel,
    CatExpenseType,
    CatSocial
]

type_defs = gql(f"""{build_type_query(models)}

{convert_table_to_schema(models)}
""")

query = QueryType()

#schema = make_executable_schema(type_defs, query)

# root resolver (discarding the first argument)
@query.field("hello")
def resolver_hello(_,  info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent