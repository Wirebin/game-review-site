from app import app
import account
from flask import render_template, session


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
		
