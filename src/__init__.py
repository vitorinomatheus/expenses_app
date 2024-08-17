from imports import *

app = Flask(__name__)

CORS(app)


app.config.from_envvar('EXPENSESAPP_SETTINGS')
db = SQLAlchemy(app)

@app.route('/')
def init():
    returnstring = Expense.get_schema()
    return f"{returnstring}"

app.run()