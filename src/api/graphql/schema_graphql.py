from ariadne import gql, QueryType, make_executable_schema
from .graphql_tools import build_type_query, convert_table_to_schema

from infra.models.user import User
from infra.models.expense import Expense
from infra.models.categories.cat_budget_impact import CatBudgetImpact
from infra.models.categories.cat_emotional import CatEmotional
from infra.models.categories.cat_expense_feel import CatExpenseFeel
from infra.models.categories.cat_expense_type import CatExpenseType
from infra.models.categories.cat_social import CatSocial

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