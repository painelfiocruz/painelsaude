from app import app
from app.models import LoginService, login
from ..models.login import UserLogin, login_schema, logins_schema
from flask import jsonify, request
import json
from ..helpers.helper import token_required, auth

@app.route('/', methods=['POST'])
@token_required
def root():
  username = request.json['username']
  password = request.json['password']
  
  # data = LoginService.login('00028249577','704609107818221painel')
  data = LoginService.login(username, password)
  
  
  return jsonify({'message': 'successfully fetched', 'data': data })


@app.route('/v1/auth', methods=['POST'])
def _auth():
    return auth()