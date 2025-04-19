from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
db = SQLAlchemy()

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(256), nullable=False)


    @property
    def password(self):
        raise AttributeError('密码不可读')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=16
        )

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.JSON, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    comments = db.relationship('Comments', backref='article', lazy='select')

    @property
    def formatted_time(self):
        return datetime.fromtimestamp(self.timestamp)
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)

    commenter = db.relationship('Users', backref='comments')

    @property
    def formatted_time(self):
        return datetime.fromtimestamp(self.timestamp)






