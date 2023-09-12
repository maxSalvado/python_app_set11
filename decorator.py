from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/upload', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'The file to upload.'
        }
    ],
    'responses': {
        200: {
            'description': 'File uploaded successfully.'
        }
    }
})
def upload_file():
    """
    Upload a file.
    ---
    consumes:
      - multipart/form-data
    produces:
      - application/json
    responses:
      200:
        description: File uploaded successfully.
    """
    uploaded_file = request.files['file']
    # Do something with the uploaded file, like saving it to disk
    # For example: uploaded_file.save('uploads/' + uploaded_file.filename)

    return jsonify(message='File uploaded successfully'), 200


if __name__ == '__main__':
    app.run(debug=True)
