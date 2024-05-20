import os
import sqlite3
import access_token
import requests as req
from time import sleep

from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash

from UserLogin import UserLogin
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from admin.admin import admin
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for, make_response


# Конфигурация
DATABASE = '/tmp/TechFix.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'TechFix.db')))
app.register_blueprint(admin, url_prefix='/admin')

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Необходимо авторизоваться"
login_manager.login_message_category = "error"

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

dbase = None
@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.teardown_appcontext
def close_db(error):
    '''Закрытие соединения с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/FAQ")
def FAQ():
    return render_template('FAQ.html')

@app.route("/about")
def about():
    return render_template('about.html', MAP_TOKEN=access_token.MAP_TOKEN)

@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user'))

    if request.method == "POST":
        user = dbase.is_username(request.form['username'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            rm = True if request.form.get('remember_me') else False
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for("user"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if len(request.form['first_name']) <= 1 or len(request.form['last_name']) <= 1: 
            flash("Неверное имя или фамилия.", "error")
            return render_template("register.html")
        if len(request.form['psw']) < 4 or len(request.form['username']) < 4: 
            flash("Пароль и логин должны иметь минимум 4 символа.", "error")
            return render_template("register.html")

        hpsw = generate_password_hash(request.form['psw'])
        res = dbase.add_user(request.form['username'], request.form['first_name'], request.form['last_name'], request.form['email'], hpsw)
        if res:
            flash("Вы успешно зарегистрированы.", "success")
            return redirect(url_for('login'))
        else:
            flash("Ошибка! Логин или email уже заняты.", "error")

    return render_template("register.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта.", "success")
    return redirect(url_for('login'))

@app.route('/user')
@login_required
def user():
    return render_template("user.html")

@app.route('/userava')
@login_required
def userava():
    img = current_user.get_avatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h

@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verify_ext(file.filename):
            try:
                img = file.read()
                res = dbase.update_useravatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватара", "error")
                flash("Аватар обновлен", "success")
            except FileNotFoundError as e:
                flash("Ошибка чтения файла", "error")
        else:
            flash("Ошибка обновления аватара", "error")

    return redirect(url_for('user'))

@app.route("/get_answer")
def get_answer():
    prompt_data = {
        "modelUri": "gpt://b1ghqjtt3mk2r9o1vjet/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.4,
            "maxTokens": "1000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты являешься консультантом интернет-магазина TechFix - \
                крупного разработчика ПО для автоматизации бизнес-процессов ремонта и продажи электротехники. \
                Некоторая информация, касательно ПО: \
                Программное средство предлагает ряд преимуществ, включая: \
                Упрощение учета и отслеживания заказов и ресурсов; \
                Генерацию отчетов для анализа эффективности работы предприятия; \
                Сокращение времени, затрачиваемого на административные задачи. \
                Наше программное средство разработано с учетом совместимости. \
                Оно может интегрироваться с существующими системами, такими как системы учета, \
                электронные платежные системы и другими, для обмена информацией и более плавного взаимодействия \
                Для установки программного средства требуется компьютер или сервер с операционной системой, \
                отвечающей минимальным требованиям (например, Windows 10, Ubuntu 18.04 и т.д.), \
                а также достаточным объемом оперативной памяти и свободного дискового пространства. \
                Точные требования указаны в документации к программному средству. \
                Твоей задачей является отвечать на вопросы посетителей сайта, который в перспективе могут \
                стать клиентами. Последующие запросы будут исходить от посетителей интернет-магазина, то есть ты \
                должен отвечать им на ""Вы"" в соответствии с заданным контекстом."
            },
            {
                "role": "user",
                "text": request.args["q"]
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {access_token.GPT_TOKEN}"
    }

    response = req.post(url, headers=headers, json=prompt_data)
    result_text = response.json()["result"]["alternatives"][0]["message"]["text"]

    return { "msg" : result_text }

if __name__ == "__main__":
    create_db()
    app.run(debug=True)