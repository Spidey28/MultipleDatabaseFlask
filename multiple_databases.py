from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask application and database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://hfyovmpj:cO2Rkv8xBIrfnj-Ub6ZY53pF4X1FufZU@satao.db.elephantsql.com:5432/hfyovmpj"

# binds multiple database definition
app.config['SQLALCHEMY_BINDS'] = {
    "mysql": "mysql://urmpate8nhqeygh6:31yEIWFIWlXUbcgA6cBV@bdfw9exjbrwrnig1agn8-mysql.services.clever-cloud.com:3306/bdfw9exjbrwrnig1agn8",  # Used cloud clever for mysql instance
    "postgres": "postgres://hfyovmpj:cO2Rkv8xBIrfnj-Ub6ZY53pF4X1FufZU@satao.db.elephantsql.com:5432/hfyovmpj"  # Used ElephantSql for postgre instance on cloud
}

db = SQLAlchemy(app)

class Superhero(db.Model):
    __bind_key__ = 'postgres'

    id = db.Column(db.Integer, primary_key=True)
    superhero = db.Column(db.String(80), unique=True, nullable=False)

class Realname(db.Model):
    __bind_key__ = 'mysql'

    id = db.Column(db.Integer, primary_key=True)
    realname = db.Column(db.String(80), unique=True, nullable=False)


# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Superhero,
                   methods=['GET'],
                   collection_name='PostgreSQL',
                   url_prefix='/')

manager.create_api(Realname,
                   methods=['GET'],
                   collection_name='MySQL',
                   url_prefix='/')

# start the flask loop
app.run(debug=False)
