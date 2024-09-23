from app import db
from sqlalchemy.sql import text
from flask import session, request, abort


def create_post(title, content, game):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    sql = text("""INSERT INTO posts (user_id, game_id, title, content)
                  VALUES (:user_id, :game_id, :title, :content)""")
    db.session.execute(sql, {"user_id":session.get("user_id"),
                             "game_id":game.id,
                             "title":title,
                             "content":content})
    db.session.commit()
    return True
    

def create_reply(content, game, post):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    sql = text("""INSERT INTO replies (user_id, game_id, post_id, content)
                  VALUES (:user_id, :game_id, :post_id, :content)""")
    db.session.execute(sql, {"user_id":session.get("user_id"),
                             "game_id":game.id,
                             "post_id":post.id,
                             "content":content})
    db.session.commit()
    return True


def get_post_by_id(post_id):
    sql = text("""SELECT id, title, content, created_at 
                  FROM posts 
                  WHERE id=:post_id""")
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchone()

