# Exercise M2_S2

# World
USE world;

#1. Ada berapa region di database world? Ubah headernya menjadi 'Jumlah_Region'!
SELECT count(DISTINCT region) AS Jumlah_Region
FROM country;

#2. Ada berapa negara di Africa? Ubah headernya menjadi 'Jumlah_Negara'!
SELECT continent, count(Name) as Jumlah_Negara
FROM country
GROUP BY continent
HAVING continent = 'Africa';

SELECT continent, count(name) as Jumlah_Negara
FROM country
WHERE continent = 'Africa'
;

#3. Tampilkan 5 negara dengan populasi terbesar! Ubah headernya menjadi 'Nama_Negara' dan 'Populasi'!
SELECT Name as 'Nama_Negara', Population as 'Populasi'
FROM country
ORDER BY population DESC
LIMIT 5;

SELECT Name as 'Nama_Negara', format(Population, 0) as 'Populasi'
FROM country
ORDER BY population DESC
LIMIT 5;

#4. Tampilkan rata-rata harapan hidup tiap benua dan urutkan dari yang terendah! Ubah headernya menjadi 'Nama_Benua' dan 'Rata_Rata_Harapan_Hidup'!
SELECT continent AS Nama_Benua, avg(LifeExpectancy) as Rata_Rata_Harapan_Hidup
FROM country
GROUP BY Nama_Benua
ORDER BY Rata_Rata_Harapan_Hidup
;

#5. Tampilkan Jumlah region tiap benua dengan jumlah region lebih dari 3! Ubah headernya menjadi 'Nama_Benua' dan 'Jumlah_Region'!
SELECT continent as Nama_Benua, count(DISTINCT region) as Jumlah_Region
FROM country
GROUP BY continent
HAVING Jumlah_Region > 3
;

#6. Tampilkan rata-rata GNP di Afrika berdasarkan regionnya dan urutkan dari rata-rata GNP terbesar! Ubah headernya menjadi 'Nama_Region' dan 'Rata_Rata_GNP'!
SELECT region AS nama_region, avg(GNP) as Rata_Rata_GNP
FROM country
WHERE continent = 'Africa'
GROUP BY region
ORDER BY Rata_Rata_GNP DESC
;

#7. Tampilkan negara di Eropa yang memiliki nama dimulai dari huruf I
SELECT name, continent
FROM country
WHERE continent = 'Europe'
AND name LIKE 'i%'
;

#8. Tampilkan Jumlah bahasa tiap negara! Urutkan dari yg paling banyak! Ubah headernya menjadi 'Jumlah_Bahasa'
SELECT countrycode, count(DISTINCT language) as Jumlah_Bahasa
FROM countrylanguage
GROUP BY countrycode
ORDER BY Jumlah_Bahasa DESC
;

#9. Tampilkan nama negara yang panjang hurufnya 6 huruf dan berakhiran 'O'
SELECT name FROM country
WHERE name LIKE '_____o';

#10. Tampilkan 7 bahasa terbesar di Indonesia (secara persentase, dengan persentase yg dibulatkan)! Ubah headernya menjadi 'Bahasa' dan 'Persentase'
SELECT countrycode, language as Bahasa, round(percentage, 0) as Persentase
FROM countrylanguage
WHERE countrycode LIKE 'IDN'
ORDER BY Percentage DESC
LIMIT 7
;

#11. Tampilkan Continent yang memiliki GovernmentForm kurang dari 10
SELECT continent, count(DISTINCT GovernmentForm)
FROM country
GROUP BY continent
HAVING count(DISTINCT GovernmentForm) < 10
;


#12. Region mana saja yg Total GNP-nya mengalami kenaikan dari Total GNP sebelumnya (GNPOld)? Urutkan dari yg tertinggi!
SELECT region, sum(GNP) - sum(GNPOld) as Selisih
FROM country
GROUP BY region
HAVING Selisih > 0
ORDER BY Selisih DESC
;
