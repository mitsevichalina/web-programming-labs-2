from flask import Blueprint, redirect, render_template, request, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 0
    if x2 == '': x2 = 0
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mult-form')
def mult_form():
    return render_template('lab4/mult-form.html')


@lab4.route('/lab4/mult', methods = ['POST'])
def mult():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 1
    if x2 == '': x2 = 1
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/mult.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/diff-form')
def diff_form():
    return render_template('lab4/diff-form.html')


@lab4.route('/lab4/diff', methods = ['POST'])
def diff():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/diff.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/diff.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/exp-form')
def exp_form():
    return render_template('lab4/exp-form.html')


@lab4.route('/lab4/exp', methods = ['POST'])
def exp():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/exp.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 != 0 and x2 != 0:
        result = x1 ** x2
        return render_template('lab4/exp.html', x1=x1, x2=x2, result=result)
    return render_template('lab4/exp.html', error='Оба поля равны нулю!')


tree_count = 0


@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    return redirect('/lab4/tree')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized=True
            name = session.get('name', '')
        else:
            authorized=False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    elif not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)



users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Henderson', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Jordan', 'gender': 'male'},
    {'login': 'alina', 'password': '748', 'name': 'Alina Mitsevich', 'gender': 'female'},
    {'login': 'sofia', 'password': '244', 'name': 'Sofia Mironova', 'gender': 'female'},
]


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        if temperature is None or temperature.strip() == '':
            message = "Ошибка: не задана температура"
            snow = 0
        else:
            temperature = int(temperature)

            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
                snow = 0
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
                snow = 0
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С"
                snow = 3
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°С"
                snow = 2
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°С"
                snow = 1

        return render_template('/lab4/fridge.html', message=message, snow=snow)

    return render_template('/lab4/fridge.html', message=None, snow=0)


seed_price = {
    'barley': {'name': 'ячмень', 'price': 12345},
    'oats': {'name': 'овёс', 'price': 8522},
    'wheat': {'name': 'пшеница', 'price': 8722},
    'rye': {'name': 'рожь', 'price': 14111}
}


@lab4.route('/lab4/seed', methods=['GET', 'POST'])
def seed():
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if not weight:
            message = "Ошибка: укажите вес заказа."
            return render_template('lab4/seed.html', message=message)

        try:
            weight = float(weight)
        except ValueError:
            message = "Ошибка: вес должен быть числом."
            return render_template('lab4/seed.html', message=message)

        if weight <= 0:
            message = "Ошибка: вес должен быть больше 0."
            return render_template('lab4/seed.html', message=message)

        if weight > 500:
            message = "Ошибка: такого объёма сейчас нет в наличии."
            return render_template('lab4/seed.html', message=message)


        grain_info = seed_price.get(grain)
        if not grain_info:
            message = "Ошибка: некорректный выбор зерна."
            return render_template('lab4/seed.html', message=message)

        price_per_ton = grain_info['price']
        grain_name_ru = grain_info['name']
        total_price = weight * price_per_ton

        discount_message = None
        if weight > 50:
            discount = 0.1
            total_price *= (1 - discount)
            discount_message = "Применена скидка 10% за большой объём."

        message = f"Заказ успешно сформирован. Вы заказали {grain_name_ru}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб."

        return render_template('lab4/seed.html', message=message, discount=discount_message)

    return render_template('lab4/seed.html')


@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        name = request.form.get('name')

        if not login or not password or not name:
            error = 'Все поля обязательны для заполнения.'
            return render_template('lab4/register.html', error=error)

        if any(user['login'] == login for user in users):
            error = 'Логин уже занят.'
            return render_template('lab4/register.html', error=error)

        users.append({'login': login, 'password': password, 'name': name, 'gender': 'unknown'})
        return redirect('/lab4/login')

    return render_template('lab4/register.html')

@lab4.route('/lab4/users')
def users_list():
    if 'login' not in session:
        return redirect('/lab4/login')

    current_user = next(user for user in users if user['login'] == session['login'])
    return render_template('lab4/users.html', users=users, current_user=current_user)

@lab4.route('/lab4/delete', methods=['POST'])
def delete_user():
    login = request.form.get('login')
    users[:] = [user for user in users if user['login'] != login]
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/edit', methods=['GET', 'POST'])
def edit_user():
    if 'login' not in session:
        return redirect('/lab4/login')

    current_user = next(user for user in users if user['login'] == session['login'])

    if request.method == 'POST':
        new_name = request.form.get('name')
        new_password = request.form.get('password')

        if new_name:
            current_user['name'] = new_name
        if new_password:
            current_user['password'] = new_password

        return redirect('/lab4/users')

    return render_template('lab4/edit.html', user=current_user)