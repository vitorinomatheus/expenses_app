from typing import List

from flask import Flask, jsonify, request, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .api.graphql.graphql_tools import build_type_query
from .api.graphql.graphql_tools import convert_model_to_graphql_schema

from .api.graphql.graphql_schema import type_defs, schema

from .infra.database import Database

from .api.graphql.graphql_server import Server

from .constants import *