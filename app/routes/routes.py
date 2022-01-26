from app import app
from app.models import LoginService, UnidadesService, login, IreceBase
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


@app.route('/v1/get-demographic-info', methods=['GET'])
@token_required
def getData():
  data = IreceBase.IreceBase()
  print(data.getDemographicInfo())
  return jsonify({'message': 'successfully fetched', 'data': data.getDemographicInfo() })    

@app.route('/v1/get-units', methods=['GET'])
@token_required
def getDataUnits():
  return jsonify({'message': 'successfully fetched', 'data': UnidadesService.getUnits().to_dict() })    

@app.route('/v1/get-demographic-info/<nu_cnes>', methods=['GET'])
@token_required
def getDataByNuCnes(nu_cnes):
  data = IreceBase.IreceBase()
  return jsonify({'message': 'successfully fetched', 'data': data.getDemographicInfo(nu_cnes) })    
