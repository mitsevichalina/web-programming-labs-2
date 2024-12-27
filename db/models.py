from db import db
from flask_login import UserMixin

# Модель пользователя
class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    articles = db.relationship('articles', backref='author', lazy=True)  # Связь с таблицей статей

# Модель статьи
class articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    article_text = db.Column(db.Text, nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Внешний ключ для связи с пользователем
    is_public = db.Column(db.Boolean, default=False)  # Поле для публичных статей