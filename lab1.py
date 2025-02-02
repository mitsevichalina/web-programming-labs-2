from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1/")
def lab():
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
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
            &copy; Алина Мицевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <img src="''' + url_for('static', filename='lab1/oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Мицевич Алина Александровна</h1>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <img src="''' + url_for('static', filename='lab1/ngtu.png') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/python')
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
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <img src="''' + url_for('static', filename='lab1/python.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/theatre')
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
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <img src="''' + url_for('static', filename='lab1/theatre.jpg') + '''">
    </body>
</html>
'''