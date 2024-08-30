from ...infra.models.user import User
from ...infra.models.expense import Expense
from ...infra.models.categories.cat_budget_impact import CatBudgetImpact
from ...infra.models.categories.cat_emotional import CatEmotional
from ...infra.models.categories.cat_expense_feel import CatExpenseFeel
from ...infra.models.categories.cat_expense_type import CatExpenseType
from ...infra.models.categories.cat_social import CatSocial

from ...infra.declarative_model_base import BaseModel

from ...domain.services.data_service import DataService

from ...constants import *

models : list[BaseModel] = [
    User,
    Expense,
    CatBudgetImpact,
    CatEmotional,
    CatExpenseFeel,
    CatExpenseType,
    CatSocial
]