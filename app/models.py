from app import db  # Импортирует объект базы данных SQLAlchemy
from flask_login import UserMixin  # Импортирует UserMixin для интеграции с системой входа пользователей

class User(UserMixin, db.Model):  # Создает модель User, наследующую от UserMixin для работы с логином
    id = db.Column(db.Integer, primary_key=True)  # ID пользователя (первичный ключ)
    email = db.Column(db.String(120), unique=True)  # Email пользователя (уникальный)
    password = db.Column(db.String(128))  # Пароль пользователя
    attempts = db.relationship('TestAttempt', backref='user', lazy=True)  # Связь с попытками теста (один ко многим)

class TestAttempt(db.Model):  # Модель для попыток тестов
    id = db.Column(db.Integer, primary_key=True)  # ID попытки теста (первичный ключ)
    score = db.Column(db.Integer)  # Оценка за попытку
    timestamp = db.Column(db.DateTime)  # Время попытки теста
    test_type = db.Column(db.String(50))  # Тип теста (например, 'video' или 'presentation')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Внешний ключ для связи с пользователем
