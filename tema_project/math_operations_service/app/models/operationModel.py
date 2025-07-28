from ..extensions import db


class Operation(db.Model):
    __tablename__='operations'

    id = db.Column(db.Integer,
                   db.Sequence('operations_id_seq'),
                   primary_key=True)

    type =      db.Column(db.String(32),
                     nullable=False)
    operand_a = db.Column(db.Float,
                          nullable=False)

    operand_b = db.Column(db.Float,
                          nullable=True)

    result =    db.Column(db.Float,
                       nullable=False)

    timestamp = db.Column(db.DateTime,
                          server_default=db.func.now(),
                          onupdate=db.func.now())

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b

    def __repr__(self):
        if self.operand_a is not None:
            return f"<Operation: type={self.type}, operand_a={self.operand_a}, operand_b={self.operand_b}, result={self.result}>"
        else:
            return f"<Operation: type={self.type}, operand_a={self.operand_a}, result={self.result}>"