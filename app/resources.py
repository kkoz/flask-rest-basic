from flask_restful import Resource, reqparse
from .models import  User

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
      return {'status': 'success', 'message': 'User {} was created'.format(username)}
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
      return {'status': 'success', 'message': 'Successfully logged in as {}.'.format(username)}
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
    return {'message' : 'List of all users'}
  def delete(self):
    return {'message': 'Delete all users'}


class ProtectedResource(Resource):
  def get(self):
    return {'answer': 42}
