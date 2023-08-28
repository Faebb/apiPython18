from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    year = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    medio = db.Column(db.Enum(Medio))
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    __tables_args__=(db.UniqueConstraint("usuario","titulo", name="titulo_unico_album"),)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    password = db.Column(db.String(128))
    albunes = db.relationship('Album', cascade='all, delete, delete-orphan')
