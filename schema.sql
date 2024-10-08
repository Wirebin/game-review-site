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
	developer TEXT,
	publisher TEXT,
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

CREATE TABLE play_stats (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	game_id INTEGER REFERENCES games,
	status TEXT,
	score INTEGER
);

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	game_id INTEGER REFERENCES games,
	title TEXT,
	content TEXT,
	score INTEGER,
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
	content TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




