from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User(db.Model):
  def __init__(self, username, email, password):
    self.user_id = uuid.uuid4().hex
    self.username = username
    self.email = email
    self.password_hash = generate_password_hash(password)
  user_id = db.Column(db.String(32), primary_key=True)
  username = db.Column(db.String(32), index=True, unique=True)
  email = db.Column(db.String(64), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  @classmethod
  def return_all(cls):
    def to_json(x):
      return {
        'username' : x.username,
        'password' : x.password
      }
    return {'users': list(map(lambda x: to_json(x), User.query.all()))}

  @classmethod
  def delete_all(cls):
    try:
      num_rows_deleted = db.session.query(cls).delete()
      db.session.commit()
      return {'status': 'success', 'message': '{} rows deleted'.format(num_rows_deleted)}
    except:
      return {'status': 'error', 'message': 'Unknown error'}
