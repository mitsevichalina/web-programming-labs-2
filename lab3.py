from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', "аноним")
    age = request.cookies.get('age', 'неизвестен') 
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)
    

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)
    

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей.
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    # Добавка молока удорожает напиток на 30 рублей, а сахара - на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():

    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')

    if color or bg_color or font_size or font_style:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_style:
            resp.set_cookie('font_style', font_style)
        return resp
    else:

        color = request.cookies.get('color')
        bg_color = request.cookies.get('bg_color')
        font_size = request.cookies.get('font_size')
        font_style = request.cookies.get('font_style')

        resp = make_response(render_template('lab3/settings.html', 
                                             color=color, 
                                             bg_color=bg_color, 
                                             font_size=font_size, 
                                             font_style=font_style))
        return resp
    

@lab3.route('/lab3/ticket_form')
def ticket_form():
    return render_template('lab3/ticket_form.html')

@lab3.route('/lab3/ticket', methods=['POST'])
def ticket():
    fio = request.form.get('fio')
    berth = request.form.get('berth')
    bedding = 'bedding' in request.form
    luggage = 'luggage' in request.form
    age = request.form.get('age')
    departure = request.form.get('departure')
    destination = request.form.get('destination')
    date = request.form.get('date')
    insurance = 'insurance' in request.form

    if not fio or not berth or not age or not departure or not destination or not date:
        flash("Заполните все обязательные поля.")
        return redirect(url_for('lab3.ticket_form'))

    try:
        age = int(age)
        if age < 1 or age > 120:
            flash("Возраст должен быть от 1 до 120 лет.")
            return redirect(url_for('lab3.ticket_form'))
    except ValueError:
        flash("Возраст должен быть числом.")
        return redirect(url_for('lab3.ticket_form'))

    ticket_type = "Детский билет" if age < 18 else "Взрослый билет"
    price = 700 if age < 18 else 1000
    if berth in ['нижняя', 'нижняя боковая']:
        price += 100
    if bedding:
        price += 75
    if luggage:
        price += 250
    if insurance:
        price += 150

    return render_template('lab3/ticket.html', 
                           fio=fio, age=age, departure=departure, destination=destination, 
                           date=date, berth=berth, bedding=bedding, luggage=luggage, 
                           insurance=insurance, price=price, ticket_type=ticket_type)


@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))

    # Удаляем все куки
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_style')

    return resp


from flask import Blueprint, render_template, request

lab3 = Blueprint('lab3', __name__)

# Список книг
books = [
    {"title": "Война и мир", "price": 1500, "author": "Лев Толстой", "genre": "Роман"},
    {"title": "Преступление и наказание", "price": 700, "author": "Федор Достоевский", "genre": "Роман"},
    {"title": "Мастер и Маргарита", "price": 800, "author": "Михаил Булгаков", "genre": "Роман"},
    {"title": "1984", "price": 600, "author": "Джордж Оруэлл", "genre": "Фантастика"},
    {"title": "Гарри Поттер и философский камень", "price": 500, "author": "Дж.К. Роулинг", "genre": "Фэнтези"},
    {"title": "Три товарища", "price": 900, "author": "Эрих Мария Ремарк", "genre": "Роман"},
    {"title": "Алхимик", "price": 400, "author": "Пауло Коэльо", "genre": "Роман"},
    {"title": "Собачье сердце", "price": 300, "author": "Михаил Булгаков", "genre": "Сатира"},
    {"title": "Сияние", "price": 650, "author": "Стивен Кинг", "genre": "Ужасы"},
    {"title": "Тень горы", "price": 1100, "author": "Грегори Дэвид Робертс", "genre": "Роман"},
    {"title": "Убить пересмешника", "price": 750, "author": "Харпер Ли", "genre": "Роман"},
    {"title": "Великий Гэтсби", "price": 500, "author": "Фрэнсис Скотт Фицджеральд", "genre": "Роман"},
    {"title": "О дивный новый мир", "price": 600, "author": "Олдос Хаксли", "genre": "Фантастика"},
    {"title": "Маленький принц", "price": 400, "author": "Антуан де Сент-Экзюпери", "genre": "Сказка"},
    {"title": "Братья Карамазовы", "price": 1300, "author": "Федор Достоевский", "genre": "Роман"},
    {"title": "451 градус по Фаренгейту", "price": 700, "author": "Рэй Брэдбери", "genre": "Фантастика"},
    {"title": "Старик и море", "price": 450, "author": "Эрнест Хемингуэй", "genre": "Роман"},
    {"title": "На игле", "price": 800, "author": "Ирвин Уэлш", "genre": "Роман"},
    {"title": "Сказки старого Вильнюса", "price": 350, "author": "Роман Кунцевич", "genre": "Сказка"},
    {"title": "Чудо", "price": 900, "author": "Р.J. Палацио", "genre": "Роман"},
    {"title": "Золотой компас", "price": 600, "author": "Филип Пулман", "genre": "Фэнтези"},
]

# Обработчик для отображения формы поиска книг
@lab3.route('/lab3/book_search')
def book_search():
    return render_template('lab3/book_search.html')

# Обработчик для поиска книг по диапазону цен
@lab3.route('/lab3/search_results', methods=['GET'])
def search_results():
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    
    # Фильтрация книг по цене
    filtered_books = [
        book for book in books 
        if min_price <= book["price"] <= max_price
    ]
    
    return render_template('lab3/search_results.html', books=filtered_books, min_price=min_price, max_price=max_price)