--Задание 1

--Insert performers
INSERT INTO performers 
VALUES(0, 'Performer_name0');
INSERT INTO performers 
VALUES(1, 'Performer_name1');
INSERT INTO performers 
VALUES(2, 'Performer_name2');
INSERT INTO performers 
VALUES(3, 'Performer name3');

--Insert genres
INSERT INTO genres  
VALUES(0, 'Genre_name0');
INSERT INTO genres 
VALUES(1, 'Genre_name1');
INSERT INTO genres 
VALUES(2, 'Genre_name2');

--Insert albums
INSERT INTO albums  
VALUES(0, 'Album_name0', '2019-07-17');
INSERT INTO albums 
VALUES(1, 'Album_name1', '2020-07-18');
INSERT INTO albums 
VALUES(2, 'Album_name2', '2023-07-19');

--Insert tracks
INSERT INTO tracks  
VALUES(0, 'Track_name0', '00:02:20', 0);
INSERT INTO tracks 
VALUES(1, 'Track_name1', '00:05:30', 1);
INSERT INTO tracks 
VALUES(2, 'Track_name2', '00:05:40', 2);
INSERT INTO tracks  
VALUES(3, 'Track_name3', '00:05:50', 0);
INSERT INTO tracks 
VALUES(4, 'Track_name4', '00:05:60', 1);
INSERT INTO tracks 
VALUES(5, 'My Track_name5', '00:06:00', 2);

--Insert compilations
INSERT INTO compilations  
VALUES(0, 'Compilation_name0', '2019-07-17');
INSERT INTO compilations 
VALUES(1, 'Compilation_name1', '2020-07-18');
INSERT INTO compilations 
VALUES(2, 'Compilation_name2', '2023-07-19');
INSERT INTO compilations 
VALUES(3, 'Compilation_name3', '2023-07-20');

--Insert albums_performers
INSERT INTO albums_performers  
VALUES(0, 0);
INSERT INTO albums_performers 
VALUES(1, 1);
INSERT INTO albums_performers 
VALUES(2, 2);
INSERT INTO albums_performers 
VALUES(0, 3);

--Insert performers_genres
INSERT INTO performers_genres  
VALUES(0, 0);
INSERT INTO performers_genres 
VALUES(1, 1);
INSERT INTO performers_genres 
VALUES(2, 2);
INSERT INTO performers_genres 
VALUES(3, 0);

--Insert tracks_compilations
INSERT INTO tracks_compilations  
VALUES(0, 0);
INSERT INTO tracks_compilations 
VALUES(1, 1);
INSERT INTO tracks_compilations 
VALUES(2, 2);
INSERT INTO tracks_compilations 
VALUES(3, 3);
INSERT INTO tracks_compilations 
VALUES(4, 0);
INSERT INTO tracks_compilations 
VALUES(5, 2);