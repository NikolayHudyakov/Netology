--Задание 2
SELECT name, duration FROM tracks
WHERE duration = (SELECT MAX(duration) FROM tracks);

SELECT name FROM tracks
WHERE duration >= '00:03:30';

SELECT name FROM compilations
WHERE date BETWEEN '2018-01-01' AND '2020-12-30';

SELECT * FROM performers
WHERE name NOT LIKE '% %';

SELECT name FROM tracks
WHERE name LIKE '%My%';

--Задание 3
SELECT g.name, COUNT(g.id) FROM genres g 
LEFT JOIN performers_genres pg ON g.id = pg.genre_id  
GROUP BY g.name;

SELECT COUNT(t.id) FROM tracks t 
LEFT JOIN albums a ON t.album_id  = a.id  
WHERE a.date BETWEEN '2019-01-01' AND '2020-12-30';

SELECT a.name, AVG(t.duration) FROM albums a 
LEFT JOIN tracks t ON a.id = t.album_id  
GROUP BY a.name;

SELECT * FROM performers p  
LEFT JOIN albums_performers ap ON p.id = ap.performer_id
LEFT JOIN albums a ON ap.album_id = a.id 
WHERE NOT EXTRACT(year FROM a.date) = '2020';

SELECT c.name FROM compilations c  
LEFT JOIN tracks_compilations tc ON c.id = tc.compilation_id 
LEFT JOIN tracks t ON tc.track_id = t.id
LEFT join albums a ON t.album_id = a.id 
LEFT join albums_performers ap ON a.id = ap.album_id 
LEFT join performers p ON ap.performer_id = p.id 
WHERE p.name = 'Performer_name0';
