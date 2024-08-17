from typing import List

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from infra.models.user import User
from infra.models.expense import Expense
from infra.models.categories.cat_budget_impact import CatBudgetImpact
from infra.models.categories.cat_emotional import CatEmotional
from infra.models.categories.cat_expense_feel import CatExpenseFeel
from infra.models.categories.cat_expense_type import CatExpenseType
from infra.models.categories.cat_social import CatSocial

from api.graphql.graphql_tools import build_type_query