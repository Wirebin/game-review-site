from app import db
from sqlalchemy.sql import text
from flask import session, request, abort, flash


def search_query(query, page_limit, offset):
    sql = text("""SELECT id, name, description, developer, publisher, release_date, created_at
                  FROM games
                  WHERE name ILIKE :query
                  ORDER BY name ASC
                  LIMIT :limit OFFSET :offset""")
    count_sql = text("SELECT COUNT(id) FROM games WHERE name ILIKE :query")
    result = db.session.execute(sql, {"query":f'%{query}%', "limit":page_limit, "offset":offset})
    count = db.session.execute(count_sql, {"query":f'%{query}%'}).scalar()

    return result.fetchall(), count


def get_genres():
    sql = text("SELECT name FROM genres")
    result = db.session.execute(sql)
    genres = [genre[0] for genre in result.fetchall()]
    
    return genres


def get_games(limit, offset, filter="name", order="ASC"):
    filters = ["name", "avg_score", "developer", "publisher", "release_date"]
    orders = ["DESC", "ASC"]

    if filter not in filters or order not in orders:
        flash("That filter is not allowed!", "error")
        return

    sql = text(f"""SELECT id, name, description, developer, publisher, release_date, created_at
                   FROM games
                   ORDER BY {filter} {order}
                   LIMIT :limit OFFSET :offset""")
    result = db.session.execute(sql, {"limit":limit, "offset":offset, "filter":filter, "order":order})
    return result.fetchall()


def count_games():
    return db.session.execute(text("SELECT COUNT(id) FROM games")).scalar()


def get_game_by_id(game_id):
    sql = text("""SELECT name, description, release_date 
                  FROM games WHERE id=:game_id""")
    result = db.session.execute(sql, {"game_id":game_id})
    return result.fetchone()


def get_game_by_name(name):
    sql = text("""SELECT id, 
                         name, 
                         TRIM(BOTH '''' FROM description) AS description,
                         developer,
                         publisher,
                         TO_CHAR(release_date, 'FMMonth FMDDth YYYY') AS release_date
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
    
    if len(name) > 28:
        flash("Genre name is over 28 characters.", "error")
    
    sql = text("SELECT name FROM genres WHERE LOWER(name)=:name")
    result = db.session.execute(sql, {"name":name.lower()})
    genre = result.fetchone()
    if genre:
        flash(f"The genre '{name}' already exists.", "error")
    else:
        sql = text("INSERT INTO genres (name) VALUES (:name)")
        db.session.execute(sql, {"name":name.capitalize()})
        db.session.commit()
        flash(f"Genre '{name}' added successfully.", "success")
    

def add_game(name, genres, release_date):
    if session.get("csrf-token") != request.form.get("csrf-token"):
        return abort(403)

    sql = text("SELECT name FROM games WHERE LOWER(name)=:name")
    result = db.session.execute(sql, {"name":name.lower()})
    game = result.fetchone()
    if game:
        flash(f"The game already exists.", "error")
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

        flash(f"Game '{name}' successfully added to the database!", "success")


def add_to_list(user_id, game_id):
    game = get_game_by_id(game_id)
    if not game:
        flash("Failed to add game to your list.", "error")
    else:
        sql = text("""INSERT INTO play_stats (user_id, game_id, status)
                      VALUES (:user_id, :game_id, 'playing')""")
        db.session.execute(sql, {"user_id":user_id, "game_id":game_id})
        db.session.commit()
        flash("Game added to your list.", "success")


def change_status(user_id, game_id, status, score):
    game = get_game_by_id(game_id)
    if not game:
        flash("Failed to update game status.", "error")
    else:
        if score == "-":
            score = None
        else:
            sql = text("""UPDATE play_stats
                          SET status=:status, score=:score
                          WHERE user_id=:user_id AND game_id=:game_id""")
            db.session.execute(sql, {"user_id":user_id, "game_id":game_id, "status":status, "score":score})
            db.session.commit()

        flash("Game status updated.", "success")


def get_avg_scores():
    sql = text("""SELECT G.name, ROUND(AVG(S.score), 2) as avg_score
                  FROM games G
                  INNER JOIN play_stats S ON G.id=S.game_id
                  GROUP BY G.name""")
    results = db.session.execute(sql).fetchall()
    return {data.name: data.avg_score for data in results}