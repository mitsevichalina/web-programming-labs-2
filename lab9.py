from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.route('/lab9/step1', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('lab9.step2', name=name))
    return render_template('lab9/step1.html')

@lab9.route('/lab9/step2', methods=['GET', 'POST'])
def step2():
    name = request.args.get('name')
    if request.method == 'POST':
        age = request.form.get('age')
        return redirect(url_for('lab9.step3', name=name, age=age))
    return render_template('lab9/step2.html', name=name)

@lab9.route('/lab9/step3', methods=['GET', 'POST'])
def step3():
    name = request.args.get('name')
    age = request.args.get('age')
    if request.method == 'POST':
        gender = request.form.get('gender')
        return redirect(url_for('lab9.step4', name=name, age=age, gender=gender))
    return render_template('lab9/step3.html', name=name, age=age)

@lab9.route('/lab9/step4', methods=['GET', 'POST'])
def step4():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    if request.method == 'POST':
        preference1 = request.form.get('preference1')
        return redirect(url_for('lab9.step5', name=name, age=age, gender=gender, preference1=preference1))
    return render_template('lab9/step4.html', name=name, age=age, gender=gender)

@lab9.route('/lab9/step5', methods=['GET', 'POST'])
def step5():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference1 = request.args.get('preference1')
    if request.method == 'POST':
        preference2 = request.form.get('preference2')
        return redirect(url_for('lab9.result', name=name, age=age, gender=gender, preference1=preference1, preference2=preference2))
    return render_template('lab9/step5.html', name=name, age=age, gender=gender, preference1=preference1)

@lab9.route('/lab9/result')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference1 = request.args.get('preference1')
    preference2 = request.args.get('preference2')

    # Определение поздравления и картинки
    if preference1 == 'tasty':
        if preference2 == 'sweet':
            gift = 'имбирное печенье'
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