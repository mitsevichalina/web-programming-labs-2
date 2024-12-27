from flask import Blueprint, render_template, request, redirect, session
from db import db
from db.models import users, articles
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def lab():
    return render_template('lab8/lab8.html', login=current_user.login if current_user.is_authenticated else None)

@lab8.route('/lab8/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form:
        return render_template('lab8/register.html', error='Имя пользователя не должно быть пустым')

    if not password_form:
        return render_template('lab8/register.html', error='Пароль не должно быть пустым')

    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')

    password_hash = generate_password_hash(password_form)
    new_user = users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=False)
    return redirect('/lab8/')

@lab8.route('/lab8/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember = request.form.get('remember') == 'on'

    if not login_form:
        return render_template('lab8/login.html', error='Имя пользователя не должно быть пустым')

    if not password_form:
        return render_template('lab8/login.html', error='Пароль не должно быть пустым')

    user = users.query.filter_by(login=login_form).first()

    if user and check_password_hash(user.password, password_form):
        login_user(user, remember=remember)
        return redirect('/lab8/')

    return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/articles/')
def article_list():
    search_query = request.args.get('search', '')
    if current_user.is_authenticated:
        user_articles = articles.query.filter((articles.login_id == current_user.id) | (articles.is_public == True))
    else:
        user_articles = articles.query.filter_by(is_public=True)
    
    if search_query:
        user_articles = user_articles.filter(articles.title.contains(search_query) | articles.article_text.contains(search_query))
    
    user_articles = user_articles.all()
    return render_template('lab8/articles.html', articles=user_articles, login=current_user.login if current_user.is_authenticated else None)

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        article_text = request.form.get('article_text')
        is_public = request.form.get('is_public') == 'on'
        new_article = articles(title=title, article_text=article_text, login_id=current_user.id, is_public=is_public)
        db.session.add(new_article)
        db.session.commit()
        return redirect('/lab8/articles')
    return render_template('lab8/create.html')

@lab8.route('/lab8/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    article = articles.query.get_or_404(id)
    if article.login_id != current_user.id:
        return "У вас нет прав на редактирование этой статьи", 403

    if request.method == 'POST':
        article.title = request.form.get('title')
        article.article_text = request.form.get('article_text')
        article.is_public = request.form.get('is_public') == 'on'
        db.session.commit()
        return redirect('/lab8/articles')
    return render_template('lab8/edit.html', article=article)

@lab8.route('/lab8/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    article = articles.query.get_or_404(id)
    if article.login_id != current_user.id:
        return "У вас нет прав на удаление этой статьи", 403

    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/articles')