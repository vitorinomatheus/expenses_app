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
    print(type_defs)
    return "<h3> Api working! </h3>"

app.run(debug=True)