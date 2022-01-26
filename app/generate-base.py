from .controllers.criarCadastroMestre import criarCadastroMestre
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from config import host, port, passwd, database, user
from .models.conexao import Conexao
import logging
from .models import IreceBase
from .models.generateBases import  cadIndividual
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config') 

db = SQLAlchemy(app)
ma = Marshmallow(app)
con = Conexao(host, database,  user, passwd, port)
criarCadastroMestre(con)

from .models import login
from .routes import routes