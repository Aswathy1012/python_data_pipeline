import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN = os.getenv('AUTH_TOKEN', 'your_auth_token')
