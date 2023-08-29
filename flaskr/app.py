from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
with app.app_context():
    c =Cancion(titulo='Why_Are_Sundays_So_Depresing', minutos =4, segundos=35, interprete='The_Strokes')
    u = Usuario(nombre="Fauner", password="Faeb1234")
    a = Album(titulo='The_New_Abnormal', year=2019, descripcion='El mejor album de la vida', medio=Medio.DISCO)
    a.canciones.append(c)
    u.albunes.append(a)
    db.session.add(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albunes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
    print(Cancion.query.all())