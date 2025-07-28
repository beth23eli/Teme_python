import jwt
from functools import wraps
from flask import request, jsonify, current_app

def jwt_authorized(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        header = request.headers.get('Authorization', None)
        token = None

        if header and header.startswith("Bearer "):
            token = header.split(" ")[1]
        else:
            token = request.form.get("token")

        if not token:
            return jsonify({"error": "Missing or invalid token"}), 401

        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 403

        return f(*args, **kwargs)

    return decorated


def generate_jwt_token(payload):
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")

