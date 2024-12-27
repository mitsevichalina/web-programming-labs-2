from flask import Blueprint, jsonify, render_template, request, abort
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify, abort, current_app
import psycopg2
from psycopg2.extras import RealDictCursor

lab7 = Blueprint('lab7', __name__)

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='alina_mitsevich_knowledge_base',
        user='alina_mitsevich_knowledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    conn, cur = db_connect()
    cur.execute("SELECT * FROM films")
    films = cur.fetchall()
    db_close(conn, cur)
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    conn, cur = db_connect()
    if current_app.config.get('DB_TYPE') == 'postgres':
        cur.execute("SELECT * FROM films WHERE id = %s", (id,))
    else:  
        cur.execute("SELECT * FROM films WHERE id = ?", (id,))
    film = cur.fetchone()
    db_close(conn, cur)

    if not film:
        abort(404)

    return jsonify(film)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    conn, cur = db_connect()
    cur.execute("DELETE FROM films WHERE id = %s RETURNING *", (id,))
    deleted_film = cur.fetchone()
    db_close(conn, cur)

    if not deleted_film:
        abort(404)

    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()

    if not film.get('description', ''):
        return jsonify({'description': 'Заполните описание'}), 400
    elif len(film['description']) > 2000:
        return jsonify({'description': 'Описание не должно превышать 2000 символов'}), 400

    if not film.get('title') and not film.get('title_ru'):
        return jsonify({'title': 'Заполните поля с названиями'}), 400

    if not film.get('title_ru'):
        return jsonify({'title_ru': 'Заполните русское название'}), 400

    if not film.get('year'):
        return jsonify({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
        return jsonify({'year': 'Введите корректный год (1800-2100)'}), 400

    conn, cur = db_connect()

    if current_app.config.get('DB_TYPE') == 'postgres':
        cur.execute("""
            UPDATE films
            SET title = %s, title_ru = %s, year = %s, description = %s
            WHERE id = %s RETURNING *
        """, (film['title'], film['title_ru'], film['year'], film['description'], id))
    else:  
        cur.execute("""
            UPDATE films
            SET title = ?, title_ru = ?, year = ?, description = ?
            WHERE id = ? RETURNING *
        """, (film['title'], film['title_ru'], film['year'], film['description'], id))

    updated_film = cur.fetchone()
    db_close(conn, cur)

    if not updated_film:
        abort(404)

    return jsonify(updated_film)


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()

    if not film.get('description', ''):
        return jsonify({'description': 'Заполните описание'}), 400
    elif len(film['description']) > 2000:
        return jsonify({'description': 'Описание не должно превышать 2000 символов'}), 400

    if not film.get('title') and not film.get('title_ru'):
        return jsonify({'title': 'Заполните поля с названиями'}), 400

    if not film.get('title_ru'):
        return jsonify({'title_ru': 'Заполните русское название'}), 400

    if not film.get('year'):
        return jsonify({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1800 or int(film['year']) > 2100:
        return jsonify({'year': 'Введите корректный год (1800-2100)'}), 400
    
    conn, cur = db_connect()
    cur.execute("""
        INSERT INTO films (title, title_ru, year, description)
        VALUES (%s, %s, %s, %s) RETURNING *
    """, (film['title'], film['title_ru'], film['year'], film['description']))
    new_film = cur.fetchone()
    db_close(conn, cur)

    return jsonify(new_film), 201