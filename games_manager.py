from app import db
from sqlalchemy.sql import text
from flask import session, request, abort

def get_genres():
    sql = text("SELECT name FROM genres")
    result = db.session.execute(sql)
    genres = [genre[0] for genre in result.fetchall()]
    
    return genres


def get_game_by_id(game_id):
    sql = text("""SELECT name, description, release_date 
                  FROM games WHERE id=:game_id""")
    result = db.session.execute(sql, {"game_id":game_id})
    return result.fetchone()


def get_game_by_name(name):
    sql = text("""SELECT id, name, TRIM(BOTH '''' FROM description) AS description, release_date 
                  FROM games WHERE LOWER(name)=:name""")
    result = db.session.execute(sql, {"name":name.lower()})
    return result.fetchone()


def get_genre_id(name):
    sql = text("SELECT id FROM genres WHERE LOWER(name)=:name")
    result = db.session.execute(sql, {"name":name.lower()})
    return result.fetchone()[0]


def add_genre(name):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    sql = text("SELECT name FROM genres WHERE LOWER(name)=:name")
    result = db.session.execute(sql, {"name":name.lower()})
    genre = result.fetchone()
    if genre:
        return False
    else:
        sql = text("INSERT INTO genres (name) VALUES (:name)")
        db.session.execute(sql, {"name":name.capitalize()})
        db.session.commit()
        return True
    

def add_game(name, genres, release_date):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)

    sql = text("SELECT name FROM games WHERE LOWER(name)=:name")
    result = db.session.execute(sql, {"name":name.lower()})
    game = result.fetchone()
    if game:
        return False
    else:
        genre_ids = [get_genre_id(genre) for genre in genres]

        # Adds game to games db.
        sql = text("""INSERT INTO games (name, release_date) 
                            VALUES (:name, :release_date)""")
        db.session.execute(sql, {"name":name, "release_date":release_date})
        db.session.commit()
        game_id = get_game_by_name(name)

        # Connects game_ids with genre_ids
        sql = text("""INSERT INTO game_genres (game_id, genre_id)
                             VALUES (:game_id, :genre_id)""")
        for genre in genre_ids:
            db.session.execute(sql, {"game_id":game_id.id, "genre_id":genre})
        db.session.commit()
        return True

