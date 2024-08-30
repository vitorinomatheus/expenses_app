from flask import Flask, jsonify, request
from ariadne import graphql_sync
from graphql import GraphQLSchema

class Server:
    def __init__(self, app: Flask, schema: GraphQLSchema):
        self.app = app
        self.schema = schema

    def build_graphql_endpoint(self):

        @self.app.route("/graphql", methods=["POST"])
        def graphql_server():   
            data = request.get_json()

            success, result = graphql_sync(
                self.schema,
                data,
                context_value={"request": request},
                debug=self.app.debug)
            
            status_code = 200 if success else 400
            return jsonify(result), status_code