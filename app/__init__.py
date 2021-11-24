from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from config import host, port, passwd, database, user
from .models.conexao import Conexao

app = Flask(__name__)
app.config.from_object('config') 

db = SQLAlchemy(app)
ma = Marshmallow(app)
con = Conexao(host, database,  user, passwd, port)
from .models import login
from .routes import routes