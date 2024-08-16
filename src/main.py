from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

# app.config.from_object('expenses_app.default_settings')
app.config.from_envvar('EXPENSESAPP_SETTINGS')
db = SQLAlchemy(app)

@app.route('/')
def init():
    return "<h3> API IS RUNNING </h3>"

app.run()