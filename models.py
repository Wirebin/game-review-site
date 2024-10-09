from app import db
from account import get_user_by_id
from sqlalchemy import desc, and_, or_


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    developer = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Date, nullable=False)

    def formatted_date(self):
        return self.release_date.strftime("%d.%m.%Y")
    
    def format_url(self):
        return self.name.replace(" ", "-")


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref=db.backref("replies", lazy=True))
    game = db.relationship("Game", backref=db.backref("replies", lazy=True))

    def formatted_date(self):
        return self.created_at.strftime("%H:%M - %d.%m.%Y")
    
    def get_poster(self):
        poster = get_user_by_id(self.user_id)
        return poster.username
    
    def get_latest_reply(self):
        return Reply.query.filter(Reply.post_id==self.id) \
                    .order_by(desc(Reply.created_at)) \
                    .limit(1).all()


class Reply(db.Model):
    __tablename__ = "replies"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref=db.backref("user_replies", lazy=True))
    game = db.relationship("Game", backref=db.backref("game_replies", lazy=True))
    post = db.relationship("Post", backref=db.backref("post_replies", lazy=True))
    
    def formatted_date(self):
        return self.created_at.strftime("%H:%M - %d.%m.%Y")


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, nullable=False)

    def formatted_date(self):
        return self.created_at.strftime("%H:%M - %d.%m.%Y")

    def get_poster(self):
        poster = get_user_by_id(self.user_id)
        return poster.username
