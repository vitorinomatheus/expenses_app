from flask import Flask, jsonify, request
from ..graphql.graphql_schema import schema
from ariadne import graphql_sync

class Server:
    def __init__(self, app: Flask):
        self.app = app

    def build_graphql_endpoint(self):

        @self.app.route("/graphql", methods=["POST"])
        def graphql_server():   
            data = request.get_json()

            success, result = graphql_sync(
                schema,
                data,
                context_value={"request": request},
                debug=self.app.debug)
            
            status_code = 200 if success else 400
            return jsonify(result), status_code