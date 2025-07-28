from ..models.operationModel import Operation
from ..extensions import db

class OperationService:

    @staticmethod
    def _commit_operation(type_, operand_a, operand_b, result):
        operation = Operation(operand_a=operand_a, operand_b=operand_b)
        operation.type = type_
        operation.result = result

        db.session.add(operation)
        db.session.commit()

        return operation

    def factorial(self, n):
        n = int(n)
        if n < 0:
            raise ValueError("Negative not allowed")
        result = 1
        for i in range(2, n + 1):
            result *= i

        return self._commit_operation('factorial', n, None, result)


    def power(self, base, exp):
        result = base ** exp

        return self._commit_operation('power', base, exp, result)

    def fibonacci(self, n):
        n = int(n)
        if n < 0:
            raise ValueError("Negative not allowed")

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b

        return self._commit_operation('fibonacci', n, None, a)