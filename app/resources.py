from flask import Response, jsonify
from flask_restful import Resource, reqparse
from .models import  User
from flask_jwt_extended import (create_access_token,
    create_refresh_token, jwt_required, jwt_refresh_token_required,
    get_jwt_identity, get_raw_jwt, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies)
import json

registration_parser = reqparse.RequestParser()
registration_parser.add_argument('username', help='This field cannot be blank', required=True)
registration_parser.add_argument('email', help='This field cannot be blank', required=True)
registration_parser.add_argument('password', help='This field cannot be blank', required=True)

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', help='This field cannot be blank', required=True)
user_parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
  def post(self):
    data = registration_parser.parse_args()
    username = data['username']
    email = data['email']
    password = data['password']
    #Check for existing user
    if User.query.filter(((User.username == username) | (User.email == email))).first() is not None:
      return {'status': 'error', 'message': 'Username/email already in use. Please try a different one.'}
    #Create new user
    new_user = User(username=username, email=email, password=password)
    try:
      new_user.save_to_db()
      access_token = create_access_token(identity=data['username'])
      refresh_token = create_refresh_token(identity=data['username'])
      resp = {
        'status': 'success',
        'message': 'User {} was created'.format(data['username']),
        'access_token': access_token,
        'refresh_token': refresh_token
      }
      set_access_cookies(resp, access_token)
      set_refresh_cookies(resp, refresh_token)
      return resp, 200
    except:
      return {'status': 'error', 'message': 'An unknown error has occurred. Try again later.'}, 500

class UserLogin(Resource):
  def post(self):
    data = user_parser.parse_args()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user is None:
      return {'status': 'error', 'message': 'No user associated with username {}.'.format(username)}
    if user.check_password(password):
      access_token = create_access_token(identity=data['username'])
      refresh_token = create_refresh_token(identity=data['username'])
      resp = jsonify({
        'status': 'success',
        'message': 'Successfully logged in as {}.'.format(username),
        'access_token': access_token,
        'refresh_token': refresh_token
      })
      set_access_cookies(resp, access_token)
      set_refresh_cookies(resp, refresh_token)
      return resp, 200
    else:
      return {'status': 'error', 'message': 'Incorrect password.'}

class UserLogoutAccess(Resource):
  def post(self):
    return {'message': 'User Logout Access'}

class UserLogoutRefresh(Resource):
  def post(self):
    return {'message': 'User Logout Refresh'}

class TokenRefresh(Resource):
  def post(self):
    return {'message': 'Token Refresh'}

class AllUsers(Resource):
  def get(self):
    return User.return_all()
  def delete(self):
    return User.delete_all()


class ProtectedResource(Resource):
  @jwt_required
  def get(self):
    return {'answer': 42}
