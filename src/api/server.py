from . import app

@app.route("/graphql", methods=["POST"])
def graphql_server():
    return "HELLO"