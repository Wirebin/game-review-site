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
INSERT INTO genres (name) VALUES ('Farming');
INSERT INTO genres (name) VALUES ('Singleplayer');
INSERT INTO genres (name) VALUES ('Multiplayer');
INSERT INTO genres (name) VALUES ('Side Scroller');
INSERT INTO genres (name) VALUES ('Co-op');
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
WHERE genres.name IN ('Visual Novel', 'Adventure', 'Singleplayer');
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
WHERE genres.name IN ('Visual Novel', 'Adventure', 'Singleplayer');
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
WHERE genres.name IN ('Action', 'Fighting', 'Adventure', 'Singleplayer');
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
WHERE genres.name IN ('Action', 'Adventure', 'Puzzle', 'First-Person', 'Singleplayer');
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
WHERE genres.name IN ('Action', 'Adventure', 'Puzzle', 'First-Person', 'Singleplayer');
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

               CrossCode is all about how it plays! Take the best out of two popular genres, find a good balance between them and make a great game. That''s what CrossCode does. You get the puzzles of Zelda-esque dungeons and are rewarded with the great variety of equipment you know and love from RPGs. During the fast-paced battles you will use the tools you find on your journey to reveal and exploit the enemies'' weaknesses and at the same time will be able to choose equipment and skills for a more in-depth approach in fighting your enemies.
            [Steam]''',
            '2020-08-14')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Action', 'Role-Playing', 'Puzzle', 'Adventure', 'Singleplayer');
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
WHERE genres.name IN ('Action', 'Sandbox', 'Roguelike', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Kerbal Space Program',
            '''In Kerbal Space Program, take charge of the space program for the alien race known as the Kerbals. You have access to an array of parts to assemble fully-functional spacecraft that flies (or doesn’t) based on realistic aerodynamic and orbital physics. Launch your Kerbal crew into orbit and beyond (while keeping them alive) to explore moons and planets in the Kerbol solar system, constructing bases and space stations to expand the reach of your expedition.

               Kerbal Space Program features three gameplay modes. In Science Mode, perform space experiments to unlock new technology and advance the knowledge of Kerbalkind. In Career Mode, oversee every aspect of the space program, including construction, strategy, funding, upgrades, and more. In Sandbox, you are free to build any spacecraft you can think of, with all parts and technology in the game.
            [Steam]''',
            '2015-04-27')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Simulation', 'Sandbox', 'Strategy', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Valheim',
            '''Valheim is a brutal exploration and survival game for 1-10 players set in a procedurally-generated world inspired by Norse mythology. Craft powerful weapons, construct longhouses, and slay mighty foes to prove yourself to Odin!

               Explore a world shrouded in mystery. Discover distinct environments with unique enemies to battle, resources to gather and secrets to uncover! Be a viking, sail the open seas in search of lands unknown, and fight bloodthirsty monsters.

               Raise viking longhouses and build bases that offer reprieve from the dangers ahead. Customise buildings, both inside and out, with a detailed building system. Progress through building tiers to upgrade, expand and defend your base.

               Struggle to survive as you gather materials and craft weapons, armor, tools, ships, and defenses. Decorate your hearths and sharpen your blades, grow crops and vegetables, prepare food, brew meads and potions, and progress as you defeat more difficult bosses and discover new recipes and blueprints.
            [Steam]''',
            '2021-02-02')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Survival', 'Sandbox', 'Third-Person');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('OneShot',
            '''A surreal puzzle adventure game with unique mechanics / capabilities.

               You are to guide a child through a mysterious world on a mission to restore its long-dead sun.

               ...Of course, things are never that simple.

               The world knows you exist.

               The consequences are real.

               Saving the world may be impossible.

               You only have one shot.
            [Steam]''',
            '2016-12-08')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Adventure', 'Role-Playing', 'Puzzle', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Euro Truck Simulator 2',
            '''Travel across Europe as king of the road, a trucker who delivers important cargo across impressive distances! With dozens of cities to explore from the UK, Belgium, Germany, Italy, the Netherlands, Poland, and many more, your endurance, skill and speed will all be pushed to their limits. If you’ve got what it takes to be part of an elite trucking force, get behind the wheel and prove it!
            [Steam]''',
            '2012-10-18')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Simulation', 'Casual');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Stardew Valley',
            '''You''ve inherited your grandfather''s old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home? It won''t be easy. Ever since Joja Corporation came to town, the old ways of life have all but disappeared. The community center, once the town''s most vibrant hub of activity, now lies in shambles. But the valley seems full of opportunity. With a little dedication, you might just be the one to restore Stardew Valley to greatness!
            [Steam]''',
            '2016-02-26')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Adventure', 'Role-Playing', 'Casual', 'Farming');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Spin Rhythm XD',
            '''Enter the Rhythm Dimension. A homage to classic arcade rhythm games (Guitar Hero, DDR), with a modern aesthetic and soundtrack. Match colours and beats, spin, tap, flick and flow through the juiciest beats in the universe.

            Spin Rhythm XD is an electronic music rhythm game with fluid, analogue-inspired controls, stunning reactive backgrounds and fully hand-made levels.
            [Steam]''',
            '2023-03-14')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Rhythm', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('RimWorld',
            '''A sci-fi colony sim driven by an intelligent AI storyteller. Generates stories by simulating psychology, ecology, gunplay, melee combat, climate, biomes, diplomacy, interpersonal relationships, art, medicine, trade, and more. 
            [Steam]''',
            '2018-10-17')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Sandbox', 'Resource Management', 'Survival', 'Strategy', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Everhood',
            '''An UNCONVENTIONAL ADVENTURE RPG that takes place in an inexpressible world filled with amusing musical battles and strange delightful encounters. To put it simply: You are in for a ride. 
            [Steam]''',
            '2021-03-04')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Rhythm', 'Singleplayer', 'Action', 'Adventure');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Super Mario Bros.',
            '''Players control Mario, or his brother Luigi in the multiplayer mode, to traverse the Mushroom Kingdom in order to rescue Princess Toadstool from King Koopa (later named Bowser). They traverse side-scrolling stages while avoiding hazards such as enemies and pits with the aid of power-ups such as the Super Mushroom, Fire Flower, and Starman. 
            [Wikipedia]''',
            '1985-09-13')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Platformer', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Super Mario 64',
            '''In the game, Bowser, the primary antagonist of the Super Mario franchise, invades Princess Peach''s castle and hides the castle''s sources of protection, the Power Stars, in many different worlds inside magical paintings.
            [Wikipedia]''',
            '1996-06-23')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Platformer', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Cities: Skylines',
            '''Cities: Skylines is a modern take on the classic city simulation. The game introduces new game play elements to realize the thrill and hardships of creating and maintaining a real city whilst expanding on some well-established tropes of the city building experience. You''re only limited by your imagination, so take control and reach for the sky!
            [Steam]''',
            '2015-03-10')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Simulator', 'Sandbox', 'Strategy', 'Singleplayer');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('Cuphead',
            '''Cuphead is a classic run and gun action game heavily focused on boss battles. Inspired by cartoons of the 1930s, the visuals and audio are painstakingly created with the same techniques of the era, i.e. traditional hand drawn cel animation, watercolor backgrounds, and original jazz recordings.

            Play as Cuphead or Mugman (in single player or local co-op) as you traverse strange worlds, acquire new weapons, learn powerful super moves, and discover hidden secrets while you try to pay your debt back to the devil! 
            [Steam]''',
            '2017-09-29')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Platformer', 'Co-op', 'Singleplayer', 'Side Scroller');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('LittleBigPlanet',
            ''' The player controls Sackboy as he travels around the titular LittleBigPlanet, helping the eight creator curators of LittleBigPlanet with their problems in their own respective realms. Throughout the story, Sackboy tries to stop The Collector, one of the eight creator curators who has gone rogue, kidnapping the creations of LittleBigPlanet.
            [Wikipedia]''',
            '2008-10-27')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Platformer', 'Singleplayer', 'Multiplayer', 'Co-op', 'Side Scroller');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('LittleBigPlanet 2',
            '''Following the events of the first game in the series, the game takes place when an antagonist known as the Negativitron invades LittleBigPlanet and begins to suck up all its inhabitants. Sackboy must team up with a secret organization known as "The Alliance", led by Larry Da Vinci, to save LittleBigPlanet from the Negativitron.
            [Wikipedia]''',
            '2011-01-19')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Platformer', 'Singleplayer', 'Multiplayer', 'Co-op', 'Side Scroller');
-----------------------------------------------------

WITH game AS (
    INSERT INTO games (name, description, release_date)
    VALUES ('LittleBigPlanet 3',
            '''Sackboy is transported to another world, Bunkum, where he has to awaken its three missing heroes, OddSock, Toggle and Swoop, who are new playable characters. Sackboy travels through different worlds in order to free the 3 new characters and stop Newton
            [Wikipedia]''',
            '2014-11-26')
    RETURNING id
)

INSERT INTO game_genres (game_id, genre_id)
SELECT game.id, genres.id
FROM game, genres
WHERE genres.name IN ('Platformer', 'Singleplayer', 'Multiplayer', 'Co-op', 'Side Scroller');
-----------------------------------------------------


