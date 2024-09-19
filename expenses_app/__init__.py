from .builder_imports import *

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_envvar('EXPENSESAPP_SETTINGS')

    @app.teardown_appcontext
    def close_db_connection(exception):
        db = getattr(g, DB, None)
        if db is not None:
            db.remove()
            g.pop(DB, None)   

    data_repository = Repository()
    data_service = DataService(data_repository)
    graphql_resolvers = GraphQLResolvers(data_service)
    graphql_schema = GraphQLSchema(graphql_resolvers).get_schema()
    server = Server(app, graphql_schema)

    server.build_graphql_endpoint()

    return app