from flask_sqlalchemy import SQLAlchemy
form marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum
db = SQLAlchemy()

albunes_canciones = db.Table('album_cancion',\
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),\
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True))

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albunes = db.relationship('Album', secondary='album_cancion', back_populates='canciones')

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
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates='albunes')
    __tables_args__=(db.UniqueConstraint("usuario","titulo", name="titulo_unico_album"),)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    password = db.Column(db.String(128))
    albunes = db.relationship('Album', cascade='all, delete, delete-orphan')

class AlbumSchema(SQLAlchemyAutoSchema):
    medio = EnumADiccionario(atribute=('Medio'))
    class Meta:
        modal = Album
        include_relationships = True
        load_instance = True

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}
