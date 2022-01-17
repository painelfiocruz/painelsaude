from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from config import host, port, passwd, database, user
from .models.conexao import Conexao
import logging
from .models import IreceBase

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config') 

db = SQLAlchemy(app)
ma = Marshmallow(app)
con = Conexao(host, database,  user, passwd, port)
file = IreceBase.IreceBase()
file.getBase()

from .models import login
from .routes import routes