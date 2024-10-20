from app import db
from sqlalchemy.sql import text
from flask import session, request, abort, flash


def create_post(title, content, game):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    errors = []

    if len(title) < 10 or len(title) > 100:
        errors.append("The title must be between 10-100 characters.")
    if len(content) < 50:
        errors.append("The post must have at least 50 characters.")
    elif len(content) > 10000:
        errors.append("The post must be under 10000 characters.")
    
    if not errors:
        sql = text("""INSERT INTO posts (user_id, game_id, title, content)
                      VALUES (:user_id, :game_id, :title, :content)""")
        db.session.execute(sql, {"user_id":session.get("user_id"),
                                "game_id":game.id,
                                "title":title,
                                "content":content})
        db.session.commit()
        return True
    
    for error in errors:
        flash(error, "error")
    return False


def create_reply(content, game, post):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    if len(content) < 25:
        flash("A reply must be at least 25 characters.", "error")
    elif len(content) > 10000:
        flash("A reply must be at most 10000 characters.", "error")
    else:
        sql = text("""INSERT INTO replies (user_id, game_id, post_id, content)
                      VALUES (:user_id, :game_id, :post_id, :content)""")
        db.session.execute(sql, {"user_id":session.get("user_id"),
                                "game_id":game.id,
                                "post_id":post.id,
                                "content":content})
        db.session.commit()
        flash("New reply created successfully.", "success")


def create_review(game, title, content, score):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)
    
    errors = []

    if not score:
        errors.append("Please select a score before publishing.")
    if len(title) < 10 or len(title) > 100:
        errors.append("The title must be between 10-100 characters.")
    if len(content) < 500:
        errors.append("The review must have at least 500 characters.")
    elif len(content) >= 20000:
        errors.append("The review must be under 20000 characters.")

    if not errors:
        sql = text("""INSERT INTO reviews (user_id, game_id, title, content, score)
                      VALUES (:user_id, :game_id, :title, :content, :score)""")
        db.session.execute(sql, {"user_id":session.get("user_id"),
                                "game_id":game.id,
                                "title":title,
                                "content":content,
                                "score":score})
        db.session.commit()
        flash("A review successfully created!", "success")
        return True
    
    for error in errors:
        flash(error, "error")
    return False


def edit_review(title, content, score, user_id, game_id, review_id):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)

    errors = []

    if not score:
        errors.append("Please select a score before publishing.")
    if len(title) < 10 or len(title) > 100:
        errors.append("The title must be between 10-100 characters.")
    if len(content) < 500:
        errors.append("The review must have at least 500 characters.")
    elif len(content) >= 20000:
        errors.append("The review must be under 20000 characters.")

    if not errors:
        sql = text("""UPDATE reviews
                    SET title=:title, content=:content, score=:score
                    WHERE user_id=:user_id AND game_id=:game_id AND id=:review_id""")
        db.session.execute(sql, {"title":title, "content":content, "score":score,
                                "user_id":user_id, "game_id":game_id, "review_id":review_id})
        db.session.commit()

        flash("Review updated successfully.", "success")
        return True
    
    for error in errors:
        flash(error, "error")
    return False


def get_post_by_id(post_id):
    sql = text("""SELECT P.id, P.title, P.content, 
                         TO_CHAR(P.created_at, 'HH24.MI, DD-MM-YYYY') as created_at, 
                         U.username
                  FROM posts P
                  INNER JOIN users U ON P.user_id=U.id
                  WHERE P.id=:post_id""")
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchone()


def get_review_by_id(review_id):
    sql = text("""SELECT R.id, R.user_id, R.title, R.content, 
                         R.score, TO_CHAR(R.created_at, 'HH24.MI, DD-MM-YYYY') as created_at, 
                         U.username
                  FROM reviews R
                  INNER JOIN users U ON R.user_id=U.id
                  WHERE R.id=:review_id""")
    result = db.session.execute(sql, {"review_id":review_id})
    return result.fetchone()


def get_posts(limit, offset, game_id):
    sql = text("""SELECT P.id, P.title, P.content, 
                         TO_CHAR(P.created_at, 'HH24.MI, DD-MM-YYYY') as created_at, 
                         U.username
                  FROM posts P
                  INNER JOIN users U ON P.user_id=U.id
                  WHERE game_id=:game_id
                  ORDER BY created_at::timestamp DESC
                  LIMIT :limit OFFSET :offset""")
    result = db.session.execute(sql, {"limit":limit, "offset":offset, "game_id":game_id})
    return result.fetchall()


def get_replies(limit, offset, game_id, post_id):
    sql = text("""SELECT R.content, TO_CHAR(R.created_at, 'HH24.MI, DD-MM-YYYY') as created_at, 
                         U.username
                  FROM replies R
                  INNER JOIN users U on R.user_id=U.id
                  WHERE game_id=:game_id AND post_id=:post_id
                  ORDER BY created_at ASC
                  LIMIT :limit OFFSET :offset""")
    result = db.session.execute(sql, {"limit":limit, "offset":offset, "game_id":game_id, "post_id":post_id})
    return result.fetchall()


def get_reviews(limit, offset, game_id):
    sql = text("""SELECT R.id, R.title, R.content, 
                         R.score, TO_CHAR(R.created_at, 'DD-MM-YYYY') as created_at, 
                         U.username
                  FROM reviews R
                  INNER JOIN Users U ON U.id=R.user_id
                  WHERE game_id=:game_id
                  ORDER BY R.created_at DESC
                  LIMIT :limit OFFSET :offset""")
    result = db.session.execute(sql, {"limit":limit, "offset":offset, "game_id":game_id})
    return result.fetchall()


def get_posts_preview(game_id):
    sql = text("""SELECT id, user_id, game_id, title, created_at
                  FROM posts
                  WHERE game_id=:game_id
                  ORDER BY created_at DESC""")
    result = db.session.execute(sql, {"game_id":game_id})
    return result.fetchall()[:3]


def get_reviews_preview(game_id):
    sql = text("""SELECT id, user_id, game_id, title, content, score
                  FROM reviews
                  WHERE game_id=:game_id
                  ORDER BY created_at DESC""")
    result = db.session.execute(sql, {"game_id":game_id})
    return result.fetchall()[:3]


def count_posts(game_id):
    sql = text("SELECT COUNT(id) FROM posts WHERE game_id=:game_id")
    return db.session.execute(sql, {"game_id":game_id}).scalar()


def count_replies(game_id, post_id):
    sql = text("SELECT COUNT(id) FROM replies WHERE game_id=:game_id AND post_id=:post_id")
    return db.session.execute(sql, {"game_id":game_id, "post_id":post_id}).scalar()


def count_reviews(game_id):
    sql = text("SELECT COUNT(id) FROM reviews WHERE game_id=:game_id")
    return db.session.execute(sql, {"game_id":game_id}).scalar()
