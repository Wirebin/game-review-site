from app import db
from sqlalchemy.sql import text

def get_genres():
    sql = text("SELECT name FROM genres")
    result = db.session.execute(sql)
    genres = [genre[0] for genre in result.fetchall()]
    
    return genres


def add_genre(name):
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
    


