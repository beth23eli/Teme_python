from flask import request, render_template
from flask import Blueprint
from .operations_service import compute_result
from .db import get_db
from .auth import jwt_authorized, generate_jwt_token


solving_bp = Blueprint("solving", __name__)

@solving_bp.route("/", methods=["GET"])
def index():
    token = generate_jwt_token({"user": "main"})
    return render_template("index.html", token=token, chosen="", operand1="", operand2="")


@solving_bp.route('/solve', methods=["POST"])
@jwt_authorized
def solve():
    token = generate_jwt_token({"user": "main"})
    error = None
    result = None

    operation = request.form.get("operation")
    a = request.form.get("operand1")
    b = request.form.get("operand2")

    try:
        first = float(a) if a else None
        second = float(b) if b else None

        if operation == "pow":
            result = compute_result(operation, first, second)
        else:
            result = compute_result(operation, first)


        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO operations (type, operand_a, operand_b, result)
            VALUES (%s, %s, %s, %s)
        """, (operation, first, second, result))

        db.commit()


    except Exception as e:
        error = f"{str(e)}"

    return render_template("index.html", result=result, error=error, token=token,  chosenflask=operation, operand1=a, operand2=b)