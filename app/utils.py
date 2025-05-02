import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your-secret-key'  # Use env variable in production

def generate_jwt(note_id):
    payload = {
        'note_id': note_id,
        'exp': datetime.utcnow() + timedelta(minutes=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
