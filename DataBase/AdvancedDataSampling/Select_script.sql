--Задание 2
SELECT name, duration FROM tracks
WHERE duration = (SELECT MAX(duration) FROM tracks);

SELECT name FROM tracks
WHERE duration >= '00:03:30';

SELECT name FROM compilations
WHERE EXTRACT(year FROM date) BETWEEN '2018' AND '2020';

SELECT * FROM performers
WHERE name NOT LIKE '% %';

SELECT name FROM tracks
WHERE name ilike '% my %' or 
	  name ilike 'my %' or 
	  name ilike '% my' or 
	  name ilike 'my';
SELECT name FROM tracks
WHERE string_to_array(lower(name), ' ') && array['my'];
SELECT name FROM tracks
WHERE name ~* 'my';

--Задание 3
SELECT g.name, COUNT(g.id) FROM genres g 
LEFT JOIN performers_genres pg ON g.id = pg.genre_id  
GROUP BY g.name;

SELECT COUNT(t.id) FROM tracks t 
LEFT JOIN albums a ON t.album_id  = a.id  
WHERE extract(year from a.date) BETWEEN '2019' AND '2020';

SELECT a.name, AVG(t.duration) FROM albums a 
LEFT JOIN tracks t ON a.id = t.album_id  
GROUP BY a.name;

Select name from performers
where name not in 
	(SELECT p.name FROM performers p
	LEFT JOIN albums_performers ap ON p.id = ap.performer_id
	LEFT JOIN albums a ON ap.album_id = a.id 
	WHERE EXTRACT(year FROM a.date) = '2020');

SELECT c.name FROM compilations c  
LEFT JOIN tracks_compilations tc ON c.id = tc.compilation_id 
LEFT JOIN tracks t ON tc.track_id = t.id
LEFT join albums a ON t.album_id = a.id 
LEFT join albums_performers ap ON a.id = ap.album_id 
LEFT join performers p ON ap.performer_id = p.id 
WHERE p.name = 'Performer_name0';

