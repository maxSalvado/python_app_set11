from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)

# Set Swagger configuration for title and URL prefix
app.config['SWAGGER'] = {
    'title': 'My Custom Swagger Title',
    'uiversion': 3,  # Use Swagger UI version 3
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/v1/swagger/"
}

# Initialize Swagger
swagger = Swagger(app)


class HelloResource(Resource):
    def get(self):
        """
        Get a friendly greeting.
        ---
        responses:
          200:
            description: A friendly greeting.
            examples:
              message: Hello There
        """
        return {"message": "Hello There"}

    def post(self):
        """
        Receive a name and other information, and return a greeting.
        ---
        parameters:
          - in: body
            name: request_body
            description: The request body with multiple fields.
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: The name to greet.
                age:
                  type: integer
                  description: The age of the person.
                email:
                  type: string
                  format: email
                  description: The email address of the person.
              required:
                - name
        responses:
          200:
            description: Greeting message.
            examples:
              application/json:
                message: "Hello John"
        """

        data = request.get_json()
        name = data.get('name', '')
        return {"message": f"Hello {name}"}





api.add_resource(HelloResource, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
