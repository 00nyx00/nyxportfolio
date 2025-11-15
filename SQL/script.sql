--1.Write an SQL query to add the following movies in the movies table:
INSERT INTO movies(id, title, year)
VALUES("60000001", "Fake Movie: Volume 1", "2003"),("60000002", "Fake Movie: Volume 2", "2004"),("60000003", "Fake Movie: Volume 3", "2005"),
("60000004", "Fake Movie: Volume 4", "2006"),("60000005", "Fake Movie: Volume 5", "2007");
--2.Write an SQL query to add the following people in the people table
INSERT INTO people(id, name, birth)
VALUES("66000001", "Aiurea Ecler", "2000"), ("66000002", "Biurea Ecler", "2001"), ("66000003", "Ciurea Ecler", "2003"), ("66000004", "Diurea Ecler", "2004");
--3.Write an SQL query linking the first three people of question 2 as stars of the film Revenge of the Sith
INSERT INTO stars (movie_id, person_id) VALUES ("60000005", "66000001"), ("60000005", "66000002"), ("60000005", "66000003");
--4.Write an SQL query linking George Lucas as director for all Star Wars films
SELECT id FROM people WHERE name = "George Lucas" AND birth = "1944";
--  get id of George Lucas as 184
INSERT INTO directors (movie_id, person_id)
VALUES ("60000001", "184"), ("60000002", "184"), ("60000003", "184"), ("60000004", "184"), ("60000005", "184");
--5. Write an SQL query where all Star Wars films are rated 8.0
INSERT INTO ratings(movie_id, rating, votes)
VALUES ("60000001", "8.0", "3627"), ("60000002", "8.0", "3289"), ("60000003", "8.0", "2374"), ("60000004", "8.0", "5632"), ("60000005", "8.0", "1734");
--6.Write an SQL query where the film Star Wars "Return of the Jedi" with a rating of 8.0
becomes a 10.0
UPDATE ratings SET rating = "10.0" WHERE movie_id = "60000002";
