import jwt
import datetime

def generate_jwt(secret_key, algorithm='HS256'):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'exp': expiration}, secret_key, algorithm=algorithm)
    return token

if __name__ == '__main__':
    secret_key = 'QWERTY'  # Use a strong, unique key
    token = generate_jwt(secret_key)
    print("Generated JWT:", token)
