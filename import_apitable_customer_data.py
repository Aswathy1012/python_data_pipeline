# Internal API - using Flask-RESTful, SQLAlchemy

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class CustomerData(db.Model):
    __tablename__ = 'customer_data'
    Customer_ID = db.Column(db.Integer, primary_key=True)
    Customer_Name = db.Column(db.String(100), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Location = db.Column(db.String(100), nullable=False)
    Date_Joined = db.Column(db.Date, nullable=False)

@app.before_request
def verify_token():
    token = request.headers.get('Authorization')
    if not token or token != f"Bearer {app.config['AUTH_TOKEN']}":
        abort(401, description="Unauthorized: Invalid or missing token")

@app.route('/api/customer_data', methods=['GET'])
def get_customer_data():
    try:
        data = CustomerData.query.all()
        result = []
        for customer in data:
            result.append({
                'Customer_ID': customer.Customer_ID,
                'Customer_Name': customer.Customer_Name,
                'Age': customer.Age,
                'Gender': customer.Gender,
                'Location': customer.Location,
                'Date_Joined': customer.Date_Joined.strftime('%Y-%m-%d')
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
