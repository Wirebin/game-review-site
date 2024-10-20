import secrets
from app import db
from flask import session, request, abort, flash
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash


def signup(username, password):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    errors = []
    
    # Check username length
    if len(username) < 2 or len(username) > 20:
        errors.append("Username must be between 2-20 characters.")
    # Check if password is within limits
    if len(password) < 8 or len(password) >= 128:
        errors.append("Password must be between 8-128 characters.")

    sql = text("SELECT id from users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    # Check existing user
    if user:
        errors.append("Username not available.")

    if not errors:
        hash_value = generate_password_hash(password)
        sql = text("""INSERT INTO users (username, password, access_level)
                      VALUES (:username, :password, 'user')""")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        flash(f"Account created for {username}. Please log in.", "success")
        return True

    for error in errors:
        flash(error, "error")
    return False
    

def login(username, password):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    sql = text("SELECT id, access_level, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user or not check_password_hash(user.password, password):
        flash("Wrong username or password. Please try again.", "error")
        return False
    else:
        session["user_id"] = user.id
        session["csfr-token"] = secrets.token_hex(16)
        return True


def logout():
    # Delete sessions
    del session["user_id"]
    del session["csfr-token"]


def get_user_by_id(user_id):
    sql = text("SELECT username, access_level FROM users WHERE id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()


def get_user_by_name(username):
    sql = text("SELECT id, access_level FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()


def get_game_from_list(user_id, game_id):
    sql = text("SELECT id, status, score FROM play_status WHERE user_id=:user_id AND game_id=:game_id")
    result = db.session.execute(sql, {"user_id":user_id, "game_id":game_id})
    return result.fetchone()


def get_user_scores(user_id):
    sql = text("""SELECT G.name, S.score 
                  FROM play_status S
                  INNER JOIN games G ON S.game_id=G.id
                  WHERE user_id=:user_id """)
    results = db.session.execute(sql, {"user_id":user_id})
    return {data.name: data.score for data in results}


def get_user_list(user_id, limit, offset):
    sql = text("""SELECT G.name, S.score, S.status, G.release_date
                  FROM play_status S
                  INNER JOIN games G ON S.game_id=G.id
                  WHERE S.user_id=:user_id
                  ORDER BY G.name ASC
                  LIMIT :limit OFFSET :offset""")
    result = db.session.execute(sql, {"user_id":user_id, "limit":limit, "offset":offset})
    return result.fetchall()


def count_list(user_id):
    sql = text("SELECT COUNT(id) FROM play_status WHERE user_id=:user_id")
    return db.session.execute(sql, {"user_id":user_id}).scalar()
