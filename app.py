from flask import redirect, url_for
import os
from flask import Flask
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from urllib.parse import quote

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'alina_mitsevich_orm'
    db_user = 'alina_mitsevich_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "alina_mitsevich_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
<!doctupe html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
    </head>
    <body>
        <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>web-сервер на flask</h1>
        <main>
        <h1 class="titlez">Лабораторные работы по WEB-программированию</h1>

        <div class="menu">
            <ol>
                <li>
                    <a href="/lab1"; style="text-decoration: none;">Первая лабораторная</a>
                </li>
                <li>
                    <a href="/lab2"; style="text-decoration: none;">Вторая лабораторная</a>
                </li>
                <li>
                    <a href="/lab3"; style="text-decoration: none;">Третья лабораторная</a>
                </li>
                <li>
                    <a href="/lab4"; style="text-decoration: none;">Четвертая лабораторная</a>
                </li>
                <li>
                    <a href="/lab5"; style="text-decoration: none;">Пятая лабораторная</a>
                </li>
                <li>
                    <a href="/lab6"; style="text-decoration: none;">Шестая лабораторная</a>
                </li>
                <li>
                    <a href="/lab7"; style="text-decoration: none;">Седьмая лабораторная</a>
                </li>
                <li>
                    <a href="/lab8"; style="text-decoration: none;">Восьмая лабораторная</a>
                </li>
            </ol>
        </div>
    </main>
        <footer>
            &copy; Алина Мицевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''