from app import db
from sqlalchemy.sql import text
from flask import session, request, abort, flash


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


def create_review(game, title, content, score):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    if len(title) < 10 or len(title) > 100:
        flash("The title must be between 10-100 characters.")
        return False
    
    if len(content) < 500:
        flash("The review must have at least 500 characters.", "error")
        return False
    elif len(content) >= 20000:
        flash("The review must be under 20000 characters.", "error")
        return False

    sql = text("""INSERT INTO reviews (user_id, game_id, title, content, score)
                  VALUES (:user_id, :game_id, :title, :content, :score)""")
    db.session.execute(sql, {"user_id":session.get("user_id"),
                             "game_id":game.id,
                             "title":title,
                             "content":content,
                             "score":score})
    db.session.commit()
    return True


def get_post_by_id(post_id):
    sql = text("""SELECT id, title, content, created_at 
                  FROM posts 
                  WHERE id=:post_id""")
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchone()


def get_review_by_id(review_id):
    sql = text("""SELECT id, user_id, title, content, score, created_at
                  FROM reviews
                  WHERE id=:review_id""")
    result = db.session.execute(sql, {"review_id":review_id})
    return result.fetchone()


def get_posts(game_id):
    sql = text("""SELECT id, user_id, game_id, title, created_at
                  FROM posts
                  WHERE game_id=:game_id
                  ORDER BY created_at DESC""")
    result = db.session.execute(sql, {"game_id":game_id})
    return result.fetchall()


def get_reviews(game_id):
    sql = text("""SELECT id, user_id, game_id, title, content, score
                  FROM reviews
                  WHERE game_id=:game_id
                  ORDER BY created_at DESC""")
    result = db.session.execute(sql, {"game_id":game_id})
    return result.fetchall()
