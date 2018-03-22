import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_CHANGES = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ['SECRET_KEY']
  JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
  JWT_TOKEN_LOCATION = ['cookies']
  JWT_COOKIE_SECURE = False if os.environ['STAGE'] == 'DEV' else True
  JWT_REFRESH_COOKIE_PATH = '/token/refresh'

  JWT_COOKIE_CSRF_PROTECT = True



