from configs.flask_config import db


class Usuario(db.Model):
    __table_args__ = {"schema": "evaluationroom"}
    __tablename__ = 'usuario'

    idusuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    correoelectronico = db.Column(db.String())
    activo = db.Column(db.Boolean())

