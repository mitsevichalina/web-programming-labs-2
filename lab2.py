from flask import Blueprint, redirect, render_template, url_for
lab2 = Blueprint('lab2', __name__)

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

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

furniture_items = [
    {
        "name": "Стул",
        "description": "Удобный стул для вашего дома.",
        "image": "lab2/chair.jpg"
    },
    {
        "name": "Стол",
        "description": "Прочный стол для обеденной зоны.",
        "image": "lab2/table.jpg"
    },
    {
        "name": "Диван",
        "description": "Комфортабельный диван для гостиной.",
        "image": "lab2/sofa.jpg"
    },
    {
        "name": "Книжный шкаф",
        "description": "Элегантный шкаф для книг и аксессуаров.",
        "image": "lab2/bookshelf.jpg"
    },
    {
        "name": "Кровать",
        "description": "Уютная кровать для комфортного сна.",
        "image": "lab2/bed.jpg"
    }
]


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):

    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:
        abort(400, description="Вы не задали имя цветка")
    flower_list.lab2end(name)
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


@lab2.route('/lab2/flowers')
def all_flowers():
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Все цветы</h1>
            <p>Всего цветов: {len(flower_list)}</p>
            <ul>
                {''.join(f'<li>{flower}</li>' for flower in flower_list)}
            </ul>
            <p><a href="{url_for('clear_flowers')}">Очистить список цветов</a></p>
        </body>
    </html>
    '''


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('all_flowers'))


@lab2.route('/lab2/add_flower/')
def add_flower_without_name():
    return "Вы не задали имя цветка", 400


@lab2.route('/lab2/example')
def example():
    name, lab_number, group, course = 'Алина Мицевич', 2, 'ФБИ-24', '3 курс'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321}
    ]
    return render_template('lab2/example.html', 
                           name=name, lab_number=lab_number, group=group, 
                           course=course, fruits=fruits)


@lab2.route('/lab2/')
def lab_index():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
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


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(url_for('calc', a=a, b=1))


@lab2.route('/books')
def book_list():
    return render_template('books.html', books=books)


@lab2.route('/furniture')
def furniture_list():
    return render_template('furniture.html', items=furniture_items)


@lab2.route('/')
def home():
    return render_template('base.html')