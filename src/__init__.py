from imports import *

app = Flask(__name__)

CORS(app)

app.config.from_envvar('EXPENSESAPP_SETTINGS')
db = SQLAlchemy(app)

models = [
    User,
    Expense,
    CatBudgetImpact,
    CatEmotional,
    CatExpenseFeel,
    CatExpenseType,
    CatSocial
]

@app.route('/')
def init():
    return build_type_query(models)

app.run(debug=True)