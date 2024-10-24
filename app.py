from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

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
            </ol>
        </div>
    </main>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <footer>
            &copy; Алина Мицевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''
