from ...infra.models.user import User
from ...infra.models.expense import Expense
from ...infra.models.categories.cat_budget_impact import CatBudgetImpact
from ...infra.models.categories.cat_emotional import CatEmotional
from ...infra.models.categories.cat_expense_feel import CatExpenseFeel
from ...infra.models.categories.cat_expense_type import CatExpenseType
from ...infra.models.categories.cat_social import CatSocial

from ...infra.models.data_analysis.user_avr_expense_feel import UserAvrExpenseFeel
from ...infra.models.data_analysis.user_avr_expense_type import UserAvrExpenseType
from ...infra.models.data_analysis.user_data_avr_emotional import UserAvrEmotional
from ...infra.models.data_analysis.user_data_avr_social import UserAvrSocial
from ...infra.models.data_analysis.user_data_avr_time_period import UserAvrTimePeriod
from ...infra.models.data_analysis.user_relation_emotional_period import UserRelationEmotionalPeriod
from ...infra.models.data_analysis.user_relation_emotional_social import UserRelationEmotionalSocial
from ...infra.models.data_analysis.user_relation_social_period import UserRelationSocialPeriod

from .graphql_mutations.graphql_login import LoginInput, LoginResponse

from ...infra.declarative_model_base import BaseModel

from ...domain.services.data_service import DataService
from ...domain.services.login_service import LoginService
from ...domain.auth_wall import AuthWall

from ...constants import *

register_models : list[BaseModel] = [
    User,
    Expense,
    CatBudgetImpact,
    CatEmotional,
    CatExpenseFeel,
    CatExpenseType,
    CatSocial
]

analysis_models: list[BaseModel] = [
    UserAvrExpenseFeel,
    UserAvrExpenseType,
    UserAvrEmotional,
    UserAvrSocial,
    UserAvrTimePeriod,
    UserRelationEmotionalPeriod,
    UserRelationEmotionalSocial,
    UserRelationSocialPeriod
]