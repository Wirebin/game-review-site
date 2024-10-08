import secrets
from app import db
from flask import session, request, abort, flash
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash


def signup(username, password):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    if len(username) < 2 or len(username) > 20:
        flash("Username must be between 2-20 characters.", "error")
        return False

    # Check if password is within limits
    if len(password) < 8 or len(password) >= 128:
        flash(f"Password is too short or long.", "error")
        return False
    
    sql = text("SELECT id from users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user:
        print("User already exists!")
        flash(f"Username not available.", "error")
        return False
    else:
        hash_value = generate_password_hash(password)
        sql = text("""INSERT INTO users (username, password, access_level)
                      VALUES (:username, :password, 'user')""")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        print(f"User {username} created!")
        return True
    

def login(username, password):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    sql = text("SELECT id, access_level, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        print("User not found!")
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["access_level"] = user.access_level
            session["csfr-token"] = secrets.token_hex(16)
            return True
        else:
            return False


def logout():
    del session["user_id"]
    del session["csfr-token"]
    del session["access_level"]


def get_user_by_id(user_id):
    sql = text("SELECT username, access_level FROM users WHERE id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()


def get_user_by_name(username):
    sql = text("SELECT id, access_level FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()


def get_game_from_list(user_id, game_id):
    sql = text("SELECT id, status, score FROM play_stats WHERE user_id=:user_id AND game_id=:game_id")
    result = db.session.execute(sql, {"user_id":user_id, "game_id":game_id})
    return result.fetchone()
