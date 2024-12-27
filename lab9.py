from flask import Blueprint, render_template, request, redirect, url_for, session

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    # Если данные уже есть в сессии, сразу показываем поздравление
    if 'name' in session and 'age' in session and 'gender' in session and 'preference1' in session and 'preference2' in session:
        return redirect(url_for('lab9.result'))
    return render_template('lab9/index.html')

@lab9.route('/lab9/step1', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('lab9.step2'))
    return render_template('lab9/step1.html')

@lab9.route('/lab9/step2', methods=['GET', 'POST'])
def step2():
    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('lab9.step3'))
    return render_template('lab9/step2.html')

@lab9.route('/lab9/step3', methods=['GET', 'POST'])
def step3():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')
        return redirect(url_for('lab9.step4'))
    return render_template('lab9/step3.html')

@lab9.route('/lab9/step4', methods=['GET', 'POST'])
def step4():
    if request.method == 'POST':
        session['preference1'] = request.form.get('preference1')
        return redirect(url_for('lab9.step5'))
    return render_template('lab9/step4.html')

@lab9.route('/lab9/step5', methods=['GET', 'POST'])
def step5():
    if request.method == 'POST':
        session['preference2'] = request.form.get('preference2')
        return redirect(url_for('lab9.result'))
    return render_template('lab9/step5.html')

@lab9.route('/lab9/result')
def result():
    # Получаем данные из сессии
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference1 = session.get('preference1')
    preference2 = session.get('preference2')

    # Определение поздравления и картинки
    if preference1 == 'tasty':
        if preference2 == 'sweet':
            gift = 'мешочек конфет'
            image = 'candy.jpg'
        else:
            gift = 'пицца'
            image = 'pizza.jpg'
    else:
        if preference2 == 'flowers':
            gift = 'букет цветов'
            image = 'flowers.jpg'
        else:
            gift = 'картина'
            image = 'art.jpg'

    # Формирование поздравления
    if int(age) < 18:
        if gender == 'male':
            greeting = f'Поздравляю тебя, {name}, желаю, чтобы ты быстро вырос, был умным и здоровым! Вот тебе подарок — {gift}.'
        else:
            greeting = f'Поздравляю тебя, {name}, желаю, чтобы ты быстро выросла, была умной и здоровой! Вот тебе подарок — {gift}.'
    else:
        if gender == 'male':
            greeting = f'Поздравляю вас, {name}, желаю вам успехов, здоровья и счастья! Вот вам подарок — {gift}.'
        else:
            greeting = f'Поздравляю вас, {name}, желаю вам успехов, здоровья и счастья! Вот вам подарок — {gift}.'

    return render_template('lab9/result.html', greeting=greeting, image=image)

@lab9.route('/lab9/reset')
def reset():
    # Очищаем сессию и перенаправляем на начальную страницу
    session.clear()
    return redirect(url_for('lab9.main'))