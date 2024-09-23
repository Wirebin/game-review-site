INSERT INTO genres (name) VALUES ('Action');
INSERT INTO genres (name) VALUES ('Platformer');
INSERT INTO genres (name) VALUES ('First-Person');
INSERT INTO genres (name) VALUES ('Third-Person');
INSERT INTO genres (name) VALUES ('Fighting');
INSERT INTO genres (name) VALUES ('Stealth');
INSERT INTO genres (name) VALUES ('Survival');
INSERT INTO genres (name) VALUES ('Rhythm');
INSERT INTO genres (name) VALUES ('Horror');
INSERT INTO genres (name) VALUES ('Adventure');
INSERT INTO genres (name) VALUES ('Visual Novel');
INSERT INTO genres (name) VALUES ('Puzzle');
INSERT INTO genres (name) VALUES ('Role-Playing');
INSERT INTO genres (name) VALUES ('Roguelike');
INSERT INTO genres (name) VALUES ('Simulation');
INSERT INTO genres (name) VALUES ('Strategy');
INSERT INTO genres (name) VALUES ('Racing');
INSERT INTO genres (name) VALUES ('MMO');
INSERT INTO genres (name) VALUES ('Sports');
INSERT INTO genres (name) VALUES ('Casual');
INSERT INTO genres (name) VALUES ('Sandbox');
INSERT INTO genres (name) VALUES ('Automation');
INSERT INTO genres (name) VALUES ('Resource Management');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Steins;Gate', 
            '''
            Steins;Gate follows a rag-tag band of tech-savvy young students who discover the means of changing  the past via mail, using a modified microwave.

            Their experiments into how far they can go with their discovery begin to spiral out of control as they become entangled in a conspiracy surrounding SERN, the organisation behind the Large Hadron Collider, and John Titor who claims to be from a dystopian future.
            [Steam]
            ''',
            '2009-10-15')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Visual Novel', 'Adventure');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Steins;Gate 0',
            '''"This is the story of the "future" that could not be saved."

            December, 2010 - Beta Worldline:

            At the end of his journey through countless worldlines filled with untold sorrows and hardship, the protagonist, Okabe Rintarou, sinks into despair and abandons all efforts of saving "her".

            As his friends grow concerned for his well-being, Okabe immerses himself in the lifestyle of a serious student in a desperate attempt to push past his guilt and grief.

            He attends a college seminar for extra credit while still struggling with trauma, where he comes across two scientists that belonged to the same school and research team as "her".

            After he publicly defends their work against skepticism during a presentation, Okabe is invited to be a test subject for a research project titled "Amadeus"— an experimental AI which uses digitized memories as artificial intelligence avatars, one containing none other than "her" memories.

            But little did he know that the project would soon draw him back into that very world of dark conspiracies he had strived to avoid.
            [vndb]''',
            '2015-12-10')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Visual Novel', 'Adventure');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Yakuza 0',
            '''Fight like hell through Tokyo and Osaka with protagonist Kazuma Kiryu and series regular Goro Majima. 
            
            Play as Kazuma Kiryu and discover how he finds himself in a world of trouble when a simple debt collection goes wrong and his mark winds up murdered. 
            
            Then, step into the silver-toed shoes of Goro Majima and explore his “normal” life as the proprietor of a cabaret club.
            [Steam]''',
            '2015-03-15')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Fighting', 'Adventure');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Mirror''s Edge',
            '''In a city where information is heavily monitored, agile couriers called Runners transport sensitive data away from prying eyes. In this seemingly utopian paradise, a crime has been committed, your sister has been framed and now you are being hunted. You are a Runner called Faith and this innovative first-person action-adventure is your story. 
            [Steam]''',
            '2009-01-13')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Adventure', 'Puzzle', 'First-Person');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Mirror''s Edge Catalyst',
            '''Follow Faith, a daring free runner, as she fights for freedom in the city of Glass. What appears to be an elegant, high-tech city on the outside, has a terrible secret hidden within. Explore every corner from the highest beautifully lit rooftops to the dark and gritty tunnels below. The city is huge, free to roam and Faith is at the center of it all. Through the first-person perspective, combine her fluid movement and advanced combat with the city''s surroundings to master the environment and uncover the conspiracy.
            [Steam]''',
            '2016-06-07')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Adventure', 'Puzzle', 'First-Person');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('FlatOut',
            '''Drivers thrown across the track, shattered fences, mangled cars, exploding tire walls, and that''s just the first corner! Use every trick, shortcut and jump as you battle 7 rivals for the championship.

               FlatOut delivers a thrilling combination of high-octane racing, smash-em-up demolition derby action and death defying stunts propelling the driver through the windshield!

               Wreak havoc, as you race on 36 tracks in fully destructible environments. Choose among 16 different upgrade-able cars that take realistic damage, affecting their appearance and drivability.

               FlatOut features 6 death defying minigames (High Jump, Long Jump, Darts, Bowling, Bullseye, Clown) and 6 destruction arenas and dirt tracks (Demolition Dash, Super Mud Mayhem, Demolition Sandpit, Circle of Eight, Super Roundabout, Crashalley Run).

               Win all of them, because if you''re not the first you''re the last!
            [Steam]''',
            '2005-07-12')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Racing', 'Action');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('FlatOut 2',
            '''Experience the drive of your life as you throw yourself around on and off the track causing fences to shatter, tire walls explode, water tanks and barrels fly across the track into other cars. And if anyone, including you, gets caught up in a big smash sit back and watch as the driver gets catapulted through the windscreen in spectacular effect. With over 5,000 destructible objects on each track and 40 deformable pieces on every car sparks are guaranteed to fly increasing the mayhem with every lap!

               Featuring an enhanced version of the original''s lauded physics engine and even faster driving track designs, FlatOut 2 also boasts a plethora of improvements, enhancements and additions to make this the definitive FlatOut experience. Twice as many vehicles, a more sophisticated career mode, additional race environments, double the number of tracks; twice as many mini-games along with many multiplayer modes (via LAN only) are just some of the exhaustive features that are included in FlatOut 2.
            [Steam]''',
            '2006-08-01')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Racing', 'Action');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Factorio',
            '''Factorio is a game in which you build and maintain factories. You will be mining resources, researching technologies, building infrastructure, automating production and fighting enemies. In the beginning you will find yourself chopping trees, mining ores and crafting mechanical arms and transport belts by hand, but in short time you can become an industrial powerhouse, with huge solar fields, oil refining and cracking, manufacture and deployment of construction and logistic robots, all for your resource needs. However this heavy exploitation of the planet''s resources does not sit nicely with the locals, so you will have to be prepared to defend yourself and your machine empire. 
            [Steam]''',
            '2020-08-14')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Survival', 'Strategy', 'Action', 'Sandbox', 'Resource Management', 'Automation');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('CrossCode',
            '''This retro-inspired 2D Action RPG might outright surprise you. CrossCode combines 16-bit SNES-style graphics with butter-smooth physics, a fast-paced combat system, and engaging puzzle mechanics, served with a gripping sci-fi story.

               CrossCode is all about how it plays! That''s why there is a free Steam demo! Go give it a try! Take the best out of two popular genres, find a good balance between them and make a great game. That''s what CrossCode does. You get the puzzles of Zelda-esque dungeons and are rewarded with the great variety of equipment you know and love from RPGs. During the fast-paced battles you will use the tools you find on your journey to reveal and exploit the enemies'' weaknesses and at the same time will be able to choose equipment and skills for a more in-depth approach in fighting your enemies.
            [Steam]''',
            '2020-08-14')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Role-Playing', 'Puzzle', 'Adventure');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('CrossCode',
            '''This retro-inspired 2D Action RPG might outright surprise you. CrossCode combines 16-bit SNES-style graphics with butter-smooth physics, a fast-paced combat system, and engaging puzzle mechanics, served with a gripping sci-fi story.

               CrossCode is all about how it plays! That''s why there is a free Steam demo! Go give it a try! Take the best out of two popular genres, find a good balance between them and make a great game. That''s what CrossCode does. You get the puzzles of Zelda-esque dungeons and are rewarded with the great variety of equipment you know and love from RPGs. During the fast-paced battles you will use the tools you find on your journey to reveal and exploit the enemies'' weaknesses and at the same time will be able to choose equipment and skills for a more in-depth approach in fighting your enemies.
            [Steam]''',
            '2020-08-14')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Role-Playing', 'Puzzle', 'Adventure');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Noita',
            '''Noita is a magical action roguelite set in a world where every pixel is physically simulated. Fight, explore, melt, burn, freeze and evaporate your way through the procedurally generated world using spells you''ve created yourself. Explore a variety of environments ranging from coal mines to freezing wastelands while delving deeper in search for unknown mysteries.
            [Steam]''',
            '2020-10-15')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Sandbox', 'Roguelike');
-----------------------------------------------------

