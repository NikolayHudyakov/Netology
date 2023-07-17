CREATE TABLE IF NOT EXISTS performers (
	id INTEGER PRIMARY KEY,
	name VARCHAR(60)
	);

CREATE TABLE IF NOT EXISTS genres (
	id INTEGER PRIMARY KEY,
	name VARCHAR(60)
	);


CREATE TABLE IF NOT EXISTS performers_genres (
	performer_id INTEGER REFERENCES performers(id),
	genre_id INTEGER REFERENCES genres(id)
	);

CREATE TABLE IF NOT EXISTS albums (
	id INTEGER PRIMARY KEY,
	name VARCHAR(60),
	date DATE
	);
	
CREATE TABLE IF NOT EXISTS albums_performers (
	album_id INTEGER REFERENCES albums(id),
	performer_id INTEGER REFERENCES performers(id)
);

CREATE TABLE IF NOT EXISTS tracks (
	id INTEGER PRIMARY KEY,
	name VARCHAR(60),
	duration interval,
	album_id INTEGER REFERENCES albums(id)
	);
	
CREATE TABLE IF NOT EXISTS compilations (
	id INTEGER PRIMARY KEY,
	name VARCHAR(60),
	date DATE
	);
	
CREATE TABLE IF NOT EXISTS tracks_compilations (
	track_id INTEGER REFERENCES tracks(id),
	compilation_id INTEGER REFERENCES compilations(id)
);