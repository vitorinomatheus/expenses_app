from typing import List

from flask import Flask, jsonify, request, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import scoped_session, Session


from .api.graphql.graphql_tools import build_type_query
from .api.graphql.graphql_tools import convert_db_model_to_graphql_schema
from .api.graphql.graphql_schema import GraphQLSchema
from .api.graphql.graphql_resolvers import GraphQLResolvers

from .infra.database import Database
from .infra.repository import Repository
from .infra.declarative_model_base import BaseModel

from .api.graphql.graphql_server import Server

from .constants import *

from .domain.services.data_service import DataService
from .domain.auth_wall import AuthWall
