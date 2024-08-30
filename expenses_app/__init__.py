from .imports import *

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_envvar('EXPENSESAPP_SETTINGS')

    @app.teardown_appcontext
    def close_db_connection(exception):
        db = getattr(g, DB, None)
        if db is not None and db is Database:
            db.close_db()    

    server = Server(app)

    server.build_graphql_endpoint()

    return app