from app import app
import account
from flask import render_template, session, request, redirect, flash, abort


@app.route("/")
def index():
	user_id = session.get("user_id")
	
	# If not logged in
	if not user_id:
		return render_template("index.html", title="Home")
	else:
		# Get the user information (username and access_level)
		user = account.get_user(user_id)
		# If user is an admin
		if user.access_level == "admin":
			return render_template("index.html", title="Home", username="admin")
		# If user is a normal user
		return render_template("index.html", title="Home", username=user.username)
		

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

@app.route("/profile")
def profile():
	if session.get("username"):
		return render_template("/account/profile.html", title="Profile")
	else:
		return abort(403)