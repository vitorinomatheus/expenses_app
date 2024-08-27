from typing import List

from flask import Flask, jsonify, request, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .infra.models.user import User, UserJsonSchema
from .infra.models.expense import Expense
from .infra.models.categories.cat_budget_impact import CatBudgetImpact
from .infra.models.categories.cat_emotional import CatEmotional
from .infra.models.categories.cat_expense_feel import CatExpenseFeel
from .infra.models.categories.cat_expense_type import CatExpenseType
from .infra.models.categories.cat_social import CatSocial

from .api.graphql.graphql_tools import build_type_query
from .api.graphql.graphql_tools import convert_model_to_graphql_schema

from .api.graphql.graphql_schema import type_defs, schema

from .infra.database import Database