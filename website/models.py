from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(100))
    game_history = db.relationship('GameHistory')
    
class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    end_game_status = db.Column(db.String(5))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    