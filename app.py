from flask import Flask, jsonify, abort, request
import os
import json
import jwt

app = Flask(__name__)

# Load JSON files
def load_json(filename):
    with open(os.path.join('data', filename), 'r') as file:
        return json.load(file)
    
@app.route('/',methods=['GET'])
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to Aswathy's API</h1>
        <p>This is a sample HTML page served by Flask.</p>
    </body>
    </html>
    '''
    return html_content

# Internal API to serve customer data
@app.route('/api/customer_data', methods=['GET'])
def get_customer_data():
    try:
        data = load_json('customer_data.json')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# External API to serve data exchange
@app.route('/api/data_exchange', methods=['GET'])
def get_data_exchange():
    try:
        data = load_json('data_exchange.json')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Token-based authentication using JWT
def verify_jwt(token):
    secret_key = os.getenv('SECRET_KEY', 'your_secret_key')
    try:
        jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        abort(401, description="Unauthorized: Token has expired")
    except jwt.InvalidTokenError:
        abort(401, description="Unauthorized: Invalid token")

@app.before_request
def verify_token():
    if request.endpoint == 'get_customer_data':
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            abort(401, description="Unauthorized: Missing token")
        token = auth_header.split(" ")[1]  # Extract token from "Bearer <token>"
        verify_jwt(token)

if __name__ == '__main__':
    app.run(debug=True)
