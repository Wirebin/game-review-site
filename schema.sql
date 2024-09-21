CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	access_level TEXT
);

CREATE TABLE games (
	id SERIAL PRIMARY KEY,
	name TEXT,
	description TEXT,
	release_date DATE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE genres (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE
);

CREATE TABLE game_genres (
	id SERIAL PRIMARY KEY,
	game_id INTEGER REFERENCES games,
	genre_id INTEGER REFERENCES genres
);

CREATE TABLE scores (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	game_id INTEGER REFERENCES games,
	score INTEGER
);

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	game_id INTEGER REFERENCES games,
	content TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	game_id INTEGER REFERENCES games,
	title TEXT,
	content TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE replies (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	game_id INTEGER REFERENCES games,
	post_id INTEGER REFERENCES posts,
	reply_count INTEGER,
	content TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




