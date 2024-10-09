# Game Review Site
This is a web app where you can review games and have discussions with other people about them.
The site allows you to make an account and give scores to different games. Reviews and discussion posts require an account.
There are 2 access levels, one for standard users and another for an admin. An admin can add new games to the database and 
remove/edit reviews and discussion posts if needed.

The site features are:
* The user can create an account, log in and out.
* The user can search for different games using a search feature.
* The user can give games a personal score with their account.
* The user can see an average rating for games that is formed from the personal scores of all users.
* The user can write a review and publish it on the website with their account.
* The user can create discussion posts and replies to said posts with their account.
* The admin can edit and delete reviews, posts and replies if needed.
* The admin can add new games to the database through the website.

## Status

The app is still missing the ability for admins to delete and edit posts/reviews and seeing score averages. Everything else has been implemented from the feature list. There are also additional features that are still planned like improved website styling and filling out the user profile as well as the home page.

Status of features:
- [x] The user can create an account, log in and out.
- [x] The user can search for different games using a search feature.
- [x] The user can give games a personal score with their account.
- [x] The user can write a review and publish it on the website with their account.
- [x] The user can create discussion posts and replies to said posts with their account.
- [x] The admin can add new games to the database through the website.
- [ ] The admin can edit and delete reviews, posts and replies if needed.
- [ ] The user can see an average rating for games that is formed from the personal scores of all users.

Things I would still like to do:
* Fill the Home and Profile pages with something to look at.
* Create a functional 'My List' page.
* Add filters for game searching.
* Improve website style.
* Clean up some files and comment code.

## Setup Guide

NOTE: This setup shows the steps for Linux, if you are using a different OS, you might need to adjust accordingly.

1. Clone the repository:

```shell
git clone https://github.com/Wirebin/game-review-site
cd game-review-site
```

2. In the root folder, create a .env file and type the following inside it:

```
DATABASE_URL=local-database-address
SECRET_KEY=your-secret-key
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remember to replace the template values with your own.

3. Next, activate the virtual environment and install the necessary dependencies.

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run the following command in the root folder to create the needed database tables.

```shell
psql < schema.sql
```

5. Please also run the following in the root folder. It will add premade data to the database tables so that you don't need to do all of the hard work. The website will look quite empty without it:

```shell
psql < db_setup.sql
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;db_setup.sql adds 28 genres and 25 games to the database.

6. Run the application with the following:

```shell
flask --app app.py run
```

## How to use

Here are some instructions for specific functions on the website:

### Making an admin account

To make an admin account you need to edit an existing account from the database.
You need to change the 'access_level' column from 'user' to 'admin'.

Here is a simple way to do it from the terminal while in root folder:

```shell
psql -c "UPDATE users SET access_level = 'admin' WHERE username = '<username>'"
```
Replace &lt;username&gt; with your username.

### Adding games and genres

To add games and genres to the database, you need to be logged on an admin account.
After this, a control panel button will appear on the website header next to the 'log out' button.
From the control panel you can add new games and genres.

### How to make reviews or posts

First you need to find the game you want to make a review or a post for. Then click on the corresponding buttons on the game page and start writing!

