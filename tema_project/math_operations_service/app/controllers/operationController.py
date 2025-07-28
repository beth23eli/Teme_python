from flask import Blueprint, request, jsonify, render_template
from ..services.operationService import OperationService
from ..auth.auth_utils import jwt_authorized, generate_jwt_token


class OperationController:
    def __init__(self):
        self.service = OperationService()
        self.blueprint = Blueprint('operations_bp', __name__)
        self._register_routes()


    def _register_routes(self):
        self.blueprint.add_url_rule("/", view_func=self.show_form, methods=["GET"])

        self.blueprint.add_url_rule("/factorial/<n>", view_func=self.factorial, methods=["GET"])

        self.blueprint.add_url_rule("/power", view_func=self.power, methods=["POST"])

        self.blueprint.add_url_rule("/fibonacci/<n>", view_func=self.fibonacci, methods=["GET"])

    def show_form(self):
        token = generate_jwt_token({"user": "frontend"})
        return render_template("index.html", token=token)

    @jwt_authorized
    def factorial(self, n):
        try:
            operation = self.service.factorial(n)

            return jsonify(self._format(operation)), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @jwt_authorized
    def power(self):
        try:
            data = request.json
            operation = self.service.power(data["base"], data["exp"])

            return jsonify(self._format(operation)), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @jwt_authorized
    def fibonacci(self, n):
        try:
            operation = self.service.fibonacci(n)

            return jsonify(self._format(operation)), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def _format(op):
        return {
            "id": op.id,
            "type": op.type,
            "operand_a": op.operand_a,
            "operand_b": op.operand_b,
            "result": op.result,
            "timestamp": op.timestamp.isoformat()
        }