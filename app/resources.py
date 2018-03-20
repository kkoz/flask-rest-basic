from flask_restful import Resource

class UserRegistration(Resource):
  def post(self):
    return {'message': 'User Registration'}

class UserLogin(Resource):
  def post(self):
    return {'message': 'User Login'}

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
