import traceback
import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from ..models import LoginService
# from .users import user_by_username
import jwt
import re

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                if not auth_token:
                    return jsonify({
                        'status': 'fail',
                        'message': 'Token is missing.'
                    }), 401
                try:
                    data = jwt.decode( auth_token, app.config['SECRET_KEY'],
                    algorithms=['HS256'] )
                    return f(*args, **kwargs)
                except Exception:
                    print(traceback.print_exc())
                    responseObject = {
                        'status': 'fail',
                        'message': 'Bearer token malformed.'
                    }
                    return jsonify(responseObject), 401
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return jsonify(responseObject), 401
        else:
            return jsonify({
                        'status': 'fail',
                        'message': 'Token is missing.'
                    }), 401 
        return f(*args, **kwargs)
    return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = request.authorization

    # if not auth or not auth.username or not auth.password:
    #     return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    username =  re.escape(request.json['username'])
    password =  re.escape(request.json['password'])
    user = LoginService.login(username, password)
    print( app.config['SECRET_KEY'] )
    # user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user :
        token = jwt.encode({
          'username': user['nome'],
          'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
          }, app.config['SECRET_KEY'] )
        print( token )  
        return jsonify({
          'message': 'Validated successfully',
          'token': token,
          'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
          })

    return jsonify({
      'message': 'could not verify',
      'WWW-Authenticate': 'Basic auth="Login required"'
      }), 401