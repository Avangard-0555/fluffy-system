from flask import render_template, redirect, url_for, request, flash  # Импортирует функции для рендеринга, перенаправлений и сообщений
from app import app, db  # Импортирует приложение Flask и объект базы данных
from app.models import User, TestAttempt  # Импортирует модели User и TestAttempt для работы с пользователями и тестами
from flask_login import login_user, logout_user, login_required  # Импортирует функции для работы с сессиями пользователей
from flask_login import current_user  # Импортирует объект текущего пользователя
from datetime import datetime  # Импортирует модуль для работы с датами и временем

# Главная страница (домашняя)
@app.route("/")
def index():
    return render_template("index.html")  # Рендерит шаблон index.html

# Страница регистрации
@app.route("/register", methods=["GET", "POST"])  # Поддерживает GET (отображение формы) и POST (обработка данных)
def register():
    if request.method == "POST":  # Если метод запроса POST (форма отправлена)
        email = request.form['email']  # Получаем email из формы
        password = request.form['password']  # Получаем пароль из формы
        user = User(email=email, password=password)  # Создаем нового пользователя
        db.session.add(user)  # Добавляем пользователя в сессию базы данных
        db.session.commit()  # Сохраняем изменения в базе данных
        flash('Account created successfully', 'success')  # Отображаем сообщение об успешной регистрации
        login_user(user)  # Выполняем вход пользователя
        return redirect(url_for('dashboard'))  # Перенаправляем на страницу панели управления
    return render_template("register.html")  # Если запрос GET, рендерим форму регистрации

# Страница входа
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":  # Если метод запроса POST (форма отправлена)
        email = request.form['email']  # Получаем email из формы
        password = request.form['password']  # Получаем пароль из формы
        user = User.query.filter_by(email=email).first()  # Ищем пользователя по email
        if user and user.password == password:  # Если пользователь найден и пароль совпадает
            login_user(user)  # Выполняем вход пользователя
            return redirect(url_for('dashboard'))  # Перенаправляем на страницу панели управления
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')  # Если ошибка, отображаем сообщение
    return render_template("login.html")  # Если запрос GET, рендерим форму входа

# Страница панели управления
@app.route("/dashboard")
@login_required  # Требует, чтобы пользователь был авторизован
def dashboard():
    return render_template("dashboard.html")  # Рендерит шаблон панели управления

# Страница курса
@app.route("/course/<type>")
@login_required
def course(type):
    return render_template("course.html", type=type)  # Рендерит шаблон курса, передавая тип курса

# Страница теста
@app.route("/test/<type>", methods=["GET", "POST"])
@login_required
def test(type):
    if request.method == "POST":  # Если метод запроса POST (форма отправлена)
        score = calculate_score()  # Рассчитываем баллы за тест
        new_attempt = TestAttempt(score=score, timestamp=datetime.utcnow(), test_type=type, user_id=current_user.id)  # Создаем новую попытку теста
        db.session.add(new_attempt)  # Добавляем попытку в сессию базы данных
        db.session.commit()  # Сохраняем изменения в базе данных
        flash('Test submitted!', 'success')  # Отображаем сообщение об успешной сдаче теста
        return redirect(url_for('dashboard'))  # Перенаправляем на страницу панели управления
    return render_template("test.html", type=type)  # Если запрос GET, рендерим страницу теста

# Функция для расчета баллов (заглушка)
def calculate_score():
    return 8  # Возвращает 8 как пример баллов



