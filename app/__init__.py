from flask import Flask  # Импортирует класс Flask для создания приложения
from flask_sqlalchemy import SQLAlchemy  # Импортирует SQLAlchemy для работы с базой данных
from flask_login import LoginManager  # Импортирует LoginManager для управления пользователями и сессиями

app = Flask(__name__)  # Создает экземпляр Flask-приложения
app.config.from_object('config.Config')  # Загружает конфигурации из config.py

db = SQLAlchemy(app)  # Создает объект для работы с базой данных
login_manager = LoginManager(app)  # Создает объект для управления входом пользователей
login_manager.login_view = 'login'  # Устанавливает маршрут для страницы входа

# Импортирует маршруты и модели после создания объекта app, чтобы избежать циклических импортов
from app import routes, models
