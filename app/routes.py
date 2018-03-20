from app import api
from .resources import (UserRegistration, UserLogin,
    UserLogoutAccess, UserLogoutRefresh, TokenRefresh,
    AllUsers, ProtectedResource)

api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(AllUsers, '/users')
api.add_resource(ProtectedResource, '/protectedresource')


