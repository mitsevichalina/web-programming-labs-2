from flask import Blueprint, redirect, render_template, url_for
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return '''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Лабораторная работа 3</title>
</head>
<body>
    <h1>Лабораторная работа 3</h1>
    <div>
        <h2>Меню:</h2>
        <ol>
            <li><a href="/lab3/cookie">Куки</a></li>
        </ol>
    </div>
<link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
</body>
</html>
'''

@lab3.route('/lab3/cookie')
def cookie():
    return render_template('lab3.html')