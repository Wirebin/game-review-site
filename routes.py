from app import app
import account
from flask import render_template, session, request, redirect, flash, abort
import games_manager


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
			flash("Wrong username or password. Please try again.", "error")
			return redirect("#")

	
@app.route("/signup", methods=["POST", "GET"])
def signup():
	if request.method == "GET":
		return render_template("/account/signup.html", title="Sign Up")
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		
		# Check if user already exists
		if not account.signup(username, password):
			flash(f"Username not available.", "error")
			return redirect("#")
		
		# If username is free, new account is created
		else:
			flash(f"Account created for {username}. Please log in.", "info")
			return redirect("/login")


@app.route("/logout")
def logout():
	account.logout()
	return redirect("/")


@app.route("/profile/<username>")
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


@app.route("/control_panel")
def control_panel():
	return render_template("/admin/control_panel.html", title="Control Panel")


@app.route("/control_panel/add_genre", methods=["POST", "GET"])
def add_genre():
	if request.method == "GET":
		return render_template("/admin/add_genre.html", title="Add Genre")
	
	if request.method == "POST":
		name = request.form["genre_name"].capitalize()
		if not games_manager.add_genre(name):
			flash(f"The genre '{name}' already exists.")
			return redirect("#")
		else:
			flash(f"Genre '{name}' added to database.")
			return redirect("#")


