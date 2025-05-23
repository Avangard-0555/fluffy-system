import os  # Импортирует модуль для работы с операционной системой

class Config:
    # Генерирует секретный ключ для использования в сессиях и безопасности
    SECRET_KEY = os.urandom(24)  # Создает случайный 24-байтовый ключ
    # Устанавливает URI для базы данных (SQLite на локальной машине)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Путь к базе данных (файл site.db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключает отслеживание изменений в моделях базы данных
