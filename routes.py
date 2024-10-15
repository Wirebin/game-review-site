from app import app
import account
from flask import render_template, session, request, redirect, abort, url_for
import games_manager
import content_manager
from decorators import admin_required, login_required
import math
#from models import Game, Post, Reply, Review
#from sqlalchemy import and_, or_, desc

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


@app.route("/", methods=["GET"])
def index():
	if request.method == "GET":
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
		# Create pagination
		query = request.args["query"]
		page = request.args.get("page", 1, type=int)
		page_limit = 20

		offset = page * page_limit - page_limit
		filtered_games = games_manager.search_query(query, page_limit, offset)

		page_count = math.ceil(filtered_games[1] / page_limit)
		page_range = [max(1, page - 2), min(page_count, page + 2)]

		return render_template("search_result.html", 
						 		title=f"Search: {query}", results=filtered_games[0], page=page, 
								total_pages=page_count, page_range=page_range, query=query)


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "GET":
		return render_template("/account/login.html", title="Log In")
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		
		# If there was an error
		if not account.login(username, password):
			return render_template("/account/login.html", title="Sign Up", username=username)
		# If username and password are correct
		else:
			return redirect("/")

	
@app.route("/signup", methods=["POST", "GET"])
def signup():
	if request.method == "GET":
		return render_template("/account/signup.html", title="Sign Up")
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		
		# Check if user creation is possible
		if not account.signup(username, password):
			return render_template("/account/signup.html", title="Sign Up", username=username)
		# If OK, new account is created
		else:
			return redirect("/login")


@app.route("/logout", methods=["GET"])
def logout():
	if request.method == "GET":
		account.logout()
		return redirect("/")


@app.route("/profile/<username>", methods=["GET"])
@login_required
def profile(username):
	if request.method == "GET":
		user = account.get_user_by_name(username)
		# Check if user exists
		if not user:
			abort(404)
		else:
			return render_template("/account/profile.html", 
									title=f"{username}'s Profile", 
									username=username, 
									access_level = user.access_level)


@app.route("/profile", methods=["GET"])
def logged_profile():
	if request.method == "GET":
		user = session.get("user_id")
		if not user:
			return redirect("/login")
		else:
			return profile(account.get_user_by_id(user).username)
	

@app.route("/control_panel", methods=["GET"])
@admin_required
def control_panel():
	if request.method == "GET":
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
		# Create pagination
		page = request.args.get("page", 1, type=int)
		page_limit = 20
		offset = page * page_limit - page_limit
		games = games_manager.get_games(page_limit, offset)

		games_count = games_manager.count_games()
		page_count = math.ceil(games_count / page_limit)
		page_range = [max(1, page - 2), min(page_count, page + 2)]

		user_scores = {}
		if session.get("user_id"):
			user_scores = account.get_user_scores(session["user_id"])
		
		return render_template("/games/game_browse.html", user_scores=user_scores,
						 		title="Games", games=games, page=page, 
								total_pages=page_count, page_range=page_range)
	

@app.route("/games/<game_name>", methods=["POST", "GET"])
def game_page(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))
	user_id = session.get("user_id")

	if not game:
		return abort(404)
	
	if request.method == "GET":
		posts_preview = content_manager.get_posts_preview(game.id)
		reviews_preview = content_manager.get_reviews_preview(game.id)

		if not user_id:
			return render_template("/games/game_page.html", title="Overview", 
						  			game=game, posts=posts_preview,
									reviews=reviews_preview)
		else:
			list_status = account.get_game_from_list(user_id, game.id)
			return render_template("/games/game_page.html", title="Overview",
						  			game=game, posts=posts_preview, 
									reviews=reviews_preview, status=list_status)

	if request.method == "POST":
		# Adding the game to users list
		if not account.get_game_from_list(user_id, game.id):
			games_manager.add_to_list(user_id, game.id)
			return redirect("#")
		
		# If game already added to list / updating status
		games_manager.change_status(user_id, game.id, request.form["play_stats"], request.form["score"])
		return redirect("#")


@app.route("/games/<game_name>/posts", methods=["GET"])
def game_posts(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))
	if not game:
		return abort(404)
	
	if request.method == "GET":
		# Create pagination
		page = request.args.get("page", 1, type=int)
		page_limit = 20
		offset = page * page_limit - page_limit
		posts = content_manager.get_posts(page_limit, offset, game.id)

		posts_count = content_manager.count_posts(game.id)
		page_count = math.ceil(posts_count / page_limit)
		page_range = [max(1, page - 2), min(page_count, page + 2)]

		return render_template("/games/game_posts.html", title="Posts", 
								game=game, game_url=game_name,
								posts=posts, page=page, 
								total_pages=page_count, page_range=page_range)
	

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
		if not content_manager.create_post(title, content, game):
			return render_template("games/create_post.html", title=title, content=content, game=game)
		else:
			return redirect(url_for("game_posts", game_name=game.name))
		

@app.route("/games/<game_name>/posts/<post_id>", methods=["POST", "GET"])
def post_page(game_name, post_id):
	if not post_id.isdigit():
		abort(404)
	
	game = games_manager.get_game_by_name(deformat_url(game_name))
	post = content_manager.get_post_by_id(post_id)

	if not game or not post:
		return abort(404)
	
	if request.method == "GET":
		page = request.args.get("page", 1, type=int)
		page_limit = 20
		offset = page * page_limit - page_limit
		replies = content_manager.get_replies(page_limit, offset, game.id, post.id)

		replies_count = content_manager.count_replies(game.id, post.id)
		page_count = math.ceil(replies_count / page_limit)
		page_range = [max(1, page - 2), min(page_count, page + 2)]

		return render_template("games/post_page.html", title=f"{post.title}", 
								game=game, game_url=game_name,
								post=post, replies=replies, page=page, 
								total_pages=page_count, page_range=page_range)
	
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
		# Create pagination
		page = request.args.get("page", 1, type=int)
		page_limit = 20
		offset = page * page_limit - page_limit
		reviews = content_manager.get_reviews(page_limit, offset, game.id)

		reviews_count = content_manager.count_reviews(game.id)
		page_count = math.ceil(reviews_count / page_limit)
		page_range = [max(1, page - 2), min(page_count, page + 2)]

		return render_template("/games/game_reviews.html", title="Reviews", 
								game=game, game_url=game_name,
								reviews=reviews, page=page, 
								total_pages=page_count, page_range=page_range)


@app.route("/games/<game_name>/reviews/create_review", methods=["POST", "GET"])
@login_required
def create_review(game_name):
	game = games_manager.get_game_by_name(deformat_url(game_name))

	if request.method == "GET":
		return render_template("games/create_review.html", game=game, score=None)
	
	if request.method == "POST":
		title = request.form["title"]
		content = request.form["content"]
		score = request.form.get("score") 
		if not content_manager.create_review(game, title, content, score):
			return render_template("games/create_review.html", title=title,
						  			content=content, score=score, game=game)
		else:
			return redirect(url_for("game_reviews", game_name=game.name))


@app.route("/games/<game_name>/reviews/<review_id>", methods=["GET"])
def review_page(game_name, review_id):
	if request.method == "GET":
		if not review_id.isdigit():
			abort(404)

		game = games_manager.get_game_by_name(deformat_url(game_name))
		review = content_manager.get_review_by_id(review_id)
		if not game or not review:
			return abort(404)
		else:
			return render_template("games/review_page.html", game=game, review=review)
