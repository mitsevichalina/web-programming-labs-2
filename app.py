from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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

@app.route("/lab1")
def lab1():
    return '''
<!doctupe html>
<html>
    <head>
        <title>Мицевич Алина Александровна, лабораторная 1</title>
    </head>
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>
        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <a href="/menu"; style="text-decoration: none;">меню</a>

        <h2>
        Реализованные роуты
        <ol>
                <li>
                    <a href="/lab1/oak"; style="text-decoration: none;">/lab1/oak - дуб</a>
                </li>
                <li>
                    <a href="/lab1/student"; style="text-decoration: none;">/lab1/student - студент</a>
                </li>
                <li>
                    <a href="/lab1/python"; style="text-decoration: none;">/lab1/python - python</a>
                </li>
                <li>
                    <a href="/lab1/theatre"; style="text-decoration: none;">/lab1/theatre - театр</a>
                </li>
            </ol>
        </h2>
        </ol>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            &copy; Алина Мицевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Мицевич Алина Александровна</h1>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <img src="''' + url_for('static', filename='ngtu.png') + '''">
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <body>
        <p>
        Как можно кратко описать Python? Питон — это язык программирования, который 
        используется в разных областях. Он не только позволяет создавать веб и мобильные 
        приложения, но и разрабатывать программное обеспечение для ПК. Python — незаменимый 
        инструмент для обработки больших данных, математических вычислений и машинного обучения.
        </p>
        <p>
        Однако что делает Python настолько привлекательным для программистов? Во-первых, его 
        синтаксис интуитивно понятный, что делает его хорошим выбором для начинающих. Во-вторых, 
        благодаря множеству библиотек и фреймворков, а также своей гибкости, он может быть 
        использован в разных сферах: web-разработке, визуальных интерфейсах, базах данных, 
        сложных расчетах и т.д.
        </p>
        <p>
        Кроме того, Python применяется в научных исследованиях — используется для анализа 
        данных и создания моделей. Этот язык создает обилие возможностей для науки о данных.
        </p>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <img src="''' + url_for('static', filename='python.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/theatre')
def theatre():
    return '''
<!doctype html>
<html>
    <body>
        <p>
        Начало театра в Европе связано с Древней Грецией и ее религиозными ритуалами в честь 
        Диониса, бога виноградной лозы. В его честь дважды в год отмечались праздники Дионисии: 
        Большой (в городах) и Малый (в селах). Во время них совершались песнопения, так 
        называемые дифирамбы. Именно они породили и трагедию, и комедию. В первоначальном 
        варианте театральные представления проходили на открытом воздухе, в местах, способных 
        вместить всех зрителей. Чаще всего это были горные склоны с дополнительным преимуществом 
        в виде отличной акустики. Позже греки начали строить здесь первые амфитеатры.
        </p>
        <p>
        Театрализованное представление изначально ограничивалось диалогом между руководителем 
        хора - корифеем - и хором. Со временем был выбран первый актер, представленный Тесписом. 
        Второй актер появился на сцене благодаря Эсхилу, а третий - по инициативе Софокла. 
        Древние греки ценили трагедию намного выше комедии, считая ее носителем важнейших 
        ценностей: религии, патриотизма, а также демократии. Ибо давайте не будем забывать, что 
        расцвет греческого театра пришелся на V век до нашей эры, то есть на пике развития 
        афинского демократического правления.
        </p>
        <p>
        Такое положение вещей коренным образом повлияло на тематику отдельных пьес. Три 
        величайших греческих трагика - Эсхил, Софокл и Еврипид - не избегали в своих 
        произведениях военных или политических тем. Их тексты также насыщены мифологией, хотя 
        религиозные темы были наиболее близки к древнейшей из великой троицы: Эсхилу.
        </p>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <img src="''' + url_for('static', filename='theatre.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):

    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:
        abort(400, description="Вы не задали имя цветка")
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </bady>
</html>
'''

@app.route('/lab2/example')
def example():
    name, lab_number, group, course = 'Алина Мицевич', 2, 'ФБИ-24', '3 курс'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321}
    ]
    return render_template('example.html', 
                           name=name, lab_number=lab_number, group=group, 
                           course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Математические операции с числами {a} и {b}</h1>
            <p>{a} + {b} = {a + b}</p>
            <p>{a} - {b} = {a - b}</p>
            <p>{a} * {b} = {a * b}</p>
            <p>{a} / {b} = {"∞" if b == 0 else a / b}</p>
            <p>{a} <sup> {b} = {a ** b}</p>
            <p><a href="{url_for('calc_default')}">Вернуться к расчету с 1 и 1</a></p>
        </body>
    </html>
    '''

# Обработчик для перенаправления по умолчанию на calc/1/1
@app.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))

# Обработчик для перенаправления с одного числа на calc/a/1
@app.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(url_for('calc', a=a, b=1))

books = [
    {"title": "1984", "author": "Джордж Оруэлл", "genre": "Антиутопия", "pages": 328},
    {"title": "Убить пересмешника", "author": "Харпер Ли", "genre": "Классика", "pages": 281},
    {"title": "Моби Дик", "author": "Герман Мелвилл", "genre": "Приключения", "pages": 720},
    {"title": "Великий Гэтсби", "author": "Фрэнсис Скотт Фицджеральд", "genre": "Классика", "pages": 180},
    {"title": "О дивный новый мир", "author": "Олдос Хаксли", "genre": "Научная фантастика", "pages": 288},
    {"title": "Война и мир", "author": "Лев Толстой", "genre": "Исторический роман", "pages": 1225},
    {"title": "Над пропастью во ржи", "author": "Джером Д. Сэлинджер", "genre": "Классика", "pages": 277},
    {"title": "Хоббит, или Туда и обратно", "author": "Дж. Р. Р. Толкин", "genre": "Фэнтези", "pages": 310},
    {"title": "Гордость и предубеждение", "author": "Джейн Остин", "genre": "Роман", "pages": 432},
    {"title": "Одиссея", "author": "Гомер", "genre": "Эпическая поэма", "pages": 541}
]

# Обработчик для вывода списка книг
@app.route('/books')
def book_list():
    return render_template('books.html', books=books)