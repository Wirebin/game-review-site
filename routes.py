from app import app
import account
from flask import render_template, session, request, redirect, abort, url_for
import games_manager
import content_manager
from decorators import admin_required, login_required
from models import Game, Post, Reply, Review
from sqlalchemy import and_, or_, desc

def deformat_url(url):
	return url.replace("-", " ")


# Need to split this file into multiple later!
#

@app.before_request
def handle_url_formatting():
	if request.method == "GET":
		url = request.path
		if " " in url:
			return redirect(url.replace(" ", "-"))


@app.route("/")
def index():
	user_id = session.get("user_id")
	title = "Home"

	# If not logged in
	if not user_id:
		return render_template("index.html", title=title)
	else:
		# Get the user information (username and access_level)
		user = account.get_user_by_id(user_id)
		return render_template("index.html", title=title,
						 		username=user.username,
								access_level=user.access_level)
		

@app.route("/search", methods=["GET"])
def search():
	if request.method == "GET":
		query = request.args["query"]
		page = request.args.get("page", 1, type=int)
		page_limit = 20
		filtered_games = Game.query.filter(Game.name.ilike(f"%{query}%"))
		games = filtered_games.paginate(page=page, per_page=page_limit)
		
		return render_template('search_result.html', query=query, results=games)


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "GET":
		return render_template("/account/login.html", title="Log In")
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		
		# If user exists
		if account.login(username, password):
			return redirect("/")
		# If password is incorrect or user doesn't exist
		else:
			return redirect("#")

	
@app.route("/signup", methods=["POST", "GET"])
def signup():
	if request.method == "GET":
		return render_template("/account/signup.html", title="Sign Up")
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		
		# Check if user creation is possible
		if not account.signup(username, password):
			return render_template("/account/signup.html", title="Sign Up")
		# If OK, new account is created
		else:
			return redirect("/login")


@app.route("/logout")
def logout():
	account.logout()
	return redirect("/")


@app.route("/profile/<username>")
@login_required
def profile(username):
	user = account.get_user_by_name(username)
	# Check if user exists
	if not user:
		abort(404)
	else:
		return render_template("/account/profile.html", 
						 		title=f"{username}'s Profile", 
								username=username, 
								access_level = user.access_level)


@app.route("/profile")
def logged_profile():
	user = session.get("user_id")
	if not user:
		return redirect("/login")
	else:
		return profile(account.get_user_by_id(user).username)
	

@app.route("/control_panel")
@admin_required
def control_panel():
	return render_template("/admin/control_panel.html", title="Control Panel")


@app.route("/control_panel/add_genre", methods=["POST", "GET"])
@admin_required
def add_genre():
	if request.method == "GET":
		return render_template("/admin/add_genre.html", title="Add Genre")
	
	if request.method == "POST":
		name = request.form["genre_name"].capitalize()
		games_manager.add_genre(name)
		return redirect("#")


@app.route("/control_panel/add_game", methods=["POST", "GET"])
@admin_required
def add_game():
	if request.method == "GET":
		genres = games_manager.get_genres()
		return render_template("/admin/add_game.html", title="Add Game", 
								genres=genres)

	if request.method == "POST":
		name = request.form["game_name"]
		genres = request.form.getlist("genre")
		release_date = request.form["release_date"]

		games_manager.add_game(name, genres, release_date)
		return redirect("#")
		

@app.route("/games", methods=["GET"])
def game_browse():
	if request.method == "GET":
		page = request.args.get("page", 1, type=int)
		page_limit = 20
		games = Game.query.order_by(Game.name).paginate(page=page, per_page=page_limit)

		return render_template("/games/game_browse.html", title="Games", games=games)
	

@app.route("/games/<game_name>", methods=["POST", "GET"])
def game_page(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))
	user_id = session.get("user_id")

	if not game:
		return abort(404)
	
	if request.method == "GET":
		posts_preview =  Post.query.filter(and_(Post.game_id==game.id, Post.user_id==user_id)) \
								   .order_by(desc(Post.created_at)) \
								   .limit(3).all()
		reviews_preview = Review.query.filter(and_(Review.game_id==game.id, Review.user_id==user_id)) \
			 						  .order_by(desc(Review.created_at)) \
									  .limit(3).all()

		if not user_id:
			return render_template("/games/game_page.html", title="Overview", game=game, 
							 		current_page="overview", posts=posts_preview,
									reviews=reviews_preview)
		else:
			list_status = account.get_game_from_list(user_id, game.id)
			return render_template("/games/game_page.html", title="Overview", game=game, 
						  			current_page="overview", posts=posts_preview, 
									reviews=reviews_preview, status=list_status)

	if request.method == "POST":
		# Adding the game to users list
		if not account.get_game_from_list(user_id, game.id):
			games_manager.add_to_list(user_id, game.id)
			return redirect("#")
		
		# If game already added to list / updating
		games_manager.change_status(user_id, game.id, request.form["play_stats"], request.form["score"])
		return redirect("#")


@app.route("/games/<game_name>/posts", methods=["GET"])
def game_posts(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))
	if not game:
		return abort(404)
	else:
		page = request.args.get("page", 1, type=int)
		page_limit = 25
		posts = Post.query.filter_by(game_id=game.id).paginate(page=page, per_page=page_limit)
		return render_template("/games/game_posts.html", title="Posts", 
								game=game, posts=posts, current_page="posts")
	

@app.route("/games/<game_name>/posts/create_post", methods=["POST", "GET"])
@login_required
def create_post(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))
	if request.method == "GET":
		if not game:
			return abort(404)
		return render_template("games/create_post.html", game=game)
	
	if request.method == "POST":
		title = request.form["title"]
		content = request.form["content"]
		content_manager.create_post(title, content, game)

		return redirect(url_for("game_posts", game_name=game.name))
		

@app.route("/games/<game_name>/posts/<post_id>", methods=["POST", "GET"])
def post_page(game_name, post_id):
	if not post_id.isdigit():
		abort(404)
	
	game = games_manager.get_game_by_name(deformat_url(game_name))
	post = content_manager.get_post_by_id(post_id)
	reply = request.args.get("reply", 1, type=int)
	reply_limit = 10
	replies = Reply.query.filter_by(post_id=post_id).paginate(page=reply, per_page=reply_limit)

	if not game or not post:
		return abort(404)
	if request.method == "GET":
		return render_template("games/post_page.html", post=post, 
						 		game=game, replies=replies)
	if request.method == "POST":
		content = request.form["content"]
		content_manager.create_reply(content, game, post)

		return redirect("#")
		

@app.route("/games/<game_name>/reviews/", methods=["GET"])
def game_reviews(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))
	if not game:
		return abort(404)
	else:
		page = request.args.get("page", 1, type=int)
		page_limit = 10
		reviews = Review.query.filter_by(game_id=game.id).paginate(page=page, per_page=page_limit)

		return render_template("games/game_reviews.html", title="Reviews", game=game, 
						 		reviews=reviews, current_page="reviews")


@app.route("/games/<game_name>/reviews/create_review", methods=["POST", "GET"])
@login_required
def create_review(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))

	if request.method == "GET":
		return render_template("games/create_review.html", game=game)
	
	if request.method == "POST":
		title = request.form["title"]
		content = request.form["content"]
		score = request.form.get("score")
		if not content_manager.create_review(game, title, content, score):
			return render_template("games/create_review.html", game=game)
		else:
			return redirect(url_for("game_reviews", game_name=game.name))


@app.route("/games/<game_name>/reviews/<review_id>")
def review_page(game_name, review_id):
	if not review_id.isdigit():
		abort(404)

	game = games_manager.get_game_by_name(deformat_url(game_name))
	review = content_manager.get_review_by_id(review_id)
	if not game or not review:
		return abort(404)
	else:
		return render_template("games/review_page.html", game=game, review=review)
