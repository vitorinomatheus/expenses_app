from .imports import *
from ariadne import graphql_sync, graphql

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_envvar('EXPENSESAPP_SETTINGS')

    models = [
        User,
        Expense,
        CatBudgetImpact,
        CatEmotional,
        CatExpenseFeel,
        CatExpenseType,
        CatSocial
    ]

    # @app.route('/')
    # def init():
    #     print(type_defs)
    #     return "<h3> Api working! </h3>"

    # @app.route("/graphql", methods=["POST"])
    # def graphql_server():
    #     db = Database()
    #     db.init_db()
    #     data = request.get_json()

    #     teste = db.session.query(User).all()
    #     result = []

    #     for t in teste:
    #         user_json_schema = UserJsonSchema()
    #         result.append(user_json_schema.dump(t))

    #     status_code = 200
    #     return jsonify(result), status_code

        # success, result = graphql_sync(
        #     schema,
        #     data,
        #     context_value={"request": request},
        #     debug=app.debug)
        
        # status_code = 200 if success else 400
        # return jsonify(result), status_code

    app.run(debug=True)

    return app

create_app()