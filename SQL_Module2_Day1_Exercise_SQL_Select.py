## Exercise 1 SQL

USE world;
SHOW FULL TABLES;
SELECT * FROM country;

# 1.  Ada berapa negara di database world?
SELECT name FROM country;
SELECT count(name) FROM country;

# 2.  Tampilkan rata-rata harapan hidup di benua Asia!
SELECT avg(LifeExpectancy) FROM country
WHERE continent = 'Asia';

# 3.  Tampilkan total populasi di Asia Tenggara!
SELECT sum(Population) FROM country
WHERE region = 'SouthEast Asia';

# 4.  Tampilkan rata-rata GNP di benua Afrika region Eastern Africa. Gunakan alias 'Average_GNP' untuk rata-rata GNP!
SELECT avg(GNP) as 'Average_GNP'
FROM country
WHERE region = 'Eastern Africa';

# 5.  Tampilkan rata-rata Populasi pada negara yang luas areanya lebih dari 5 juta km2!
SELECT avg(Population) FROM country
WHERE SurfaceArea > 5000000;

# 6.  Ada berapa bahasa (unique) di dunia?
SELECT * FROM countrylanguage;
SELECT count(DISTINCT language) FROM countrylanguage;

# 7.  Tampilkan GNP dari 5 negara di Asia yang populasinya di atas 100 juta penduduk!
SELECT Name, GNP FROM country
WHERE continent = 'Asia' AND population > 10e7
LIMIT 5;

# 8.  Tampilkan negara di Afrika yang memiliki SurfaceArea di atas 1.200.000!
SELECT Name, SurfaceArea FROM country
WHERE continent = 'Africa' AND SurfaceArea > 1200000;

# 9.  Tampilkan negara di Asia yang sistem pemerintahannya adalah republik. Ada berapa jumlah negaranya?
SELECT Name, continent, GovernmentForm  FROM country
WHERE continent = 'Asia' AND GovernmentForm = 'Republic';

SELECT count(Name)  FROM country
WHERE continent = 'Asia' AND GovernmentForm = 'Republic';

# 10. Tampilkan jumlah negara di Eropa yang merdeka sebelum 1940!
SELECT count(Name) FROM country
WHERE continent = 'Europe' AND IndepYear < 1940;
