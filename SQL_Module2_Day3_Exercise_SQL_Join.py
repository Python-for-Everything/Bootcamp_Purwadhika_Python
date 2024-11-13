# WORLD
USE world;
SELECT * FROM city;

# 1. Tampilkan 10 kota dengan populasi terbanyak. (tampilkan nama kota, asal negara, dan populasinya)
SELECT c.Name AS city_name, co.Name AS country_name, c.Population
FROM city c
JOIN country co ON c.CountryCode = co.Code
ORDER BY c.Population DESC
LIMIT 10;


# 2. Tampilkan negara - negara di asia yang angka harapan hidupnya lebih besar dari rata-rata angka harapan hidup
# negara di benua eropa. Urutkan 10 data dari angkaharapan hidup tertinggi.
# (tampilkan, nama negara, benua, angkaharapanhidup, dan gnp).
SELECT * FROM country;

SELECT Name AS nama_negara,Continent AS benua, LifeExpectancy AS angka_harapan_hidup,GNP AS gnp
FROM country
WHERE Continent = 'Asia'
    AND LifeExpectancy > (
        SELECT AVG(LifeExpectancy)
        FROM country
        WHERE Continent = 'Europe'
    )
ORDER BY LifeExpectancy DESC
LIMIT 10;


# 3. Tampilkan 10 negara dengan persentase tertinggi yang menggunakan bahasa inggris sebagai bahasa resmi negaranya.
# (Tampilkan kode negara, nama negara, bahasa, Resmi(T/F), persentase).
SELECT * FROM country;

SELECT c.Code AS kode_negara, c.Name AS nama_negara, cl.Language AS bahasa, cl.IsOfficial AS resmi, cl.Percentage AS persentase
FROM country c
JOIN  countrylanguage cl ON c.Code = cl.CountryCode
WHERE cl.Language = 'English'
AND cl.IsOfficial = 'T'
ORDER BY cl.Percentage DESC
LIMIT 10;


# 4. Tampilkan negara, populasi negara, GNP, ibukota, dan populasi ibukota.
# DI ASEAN dan urutkan berdasarkan abjad nama negara.
#SELECT * FROM country;

SELECT c.Name AS negara, c.Population AS populasi_negara,c.GNP AS gnp,ct.Name AS ibukota, ct.Population AS populasi_ibukota
FROM country c
JOIN city ct ON c.Capital = ct.ID
WHERE c.Region = 'Southeast Asia'
ORDER BY c.Name ASC;

# 5. Tampilkan negara, populasi negara, GNP, ibukota, dan populasi ibukota.
# Di Negara G-20


SELECT c.Name AS negara, c.Population AS populasi_negara, c.GNP AS gnp,ct.Name AS ibukota, ct.Population AS populasi_ibukota
FROM country c
JOIN city ct ON c.Capital = ct.ID
WHERE c.Name IN ('Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany',
               'India', 'Indonesia', 'Italy', 'Japan', 'Mexico', 'Russia', 'Saudi Arabia',
               'South Africa', 'South Korea', 'Turkey', 'United Kingdom', 'United States')
ORDER BY c.Name ASC;


# ----------------------------------------------------------------------------------------------------------------------

# SAKILA
USE sakila;
SELECT * FROM payment;

# 1. Tampilkan 10 baris data customer id, rental id, amount, dan payment date pada table payment!
SELECT customer_id, rental_id,amount,payment_date
FROM payment
LIMIT 10;

# 2. Dari table “film”, tampilkan 10 judul film, tahun release, dan
# durasi rental di mana judul film yang ditampilkan yang dimulai dengan huruf “S”!
SELECT * FROM film;
SELECT title AS judul_film,release_year AS tahun_rilis,rental_duration AS durasi_rental
FROM film
WHERE title LIKE 'S%'
LIMIT 10;


# 3. Dari tabel “film”, tampilkan durasi rental, banyaknya film setiap durasi rental, dan rata-rata durasi film!
# Kelompokkan jumlah film dan rata-rata durasi film berdasarkan durasi rentalnya!
# Karena rata-rata durasi film angka desimal, bulatkan 2 angka di belakang koma!
SELECT * FROM FILM;
SELECT rental_duration AS durasi_rental, COUNT(*) AS jumlah_film, ROUND(AVG(length), 2) AS rata_rata_durasi_film
FROM  film
GROUP BY rental_duration
ORDER BY rental_duration;


# 4. Dari tabel film, tampilkan title, durasi film, dan juga rating yang durasi filmnya lebih dari
# rata-rata durasi film total!
# Tampilkan 25 data yang diurutkan dari durasi terlama!
SELECT * FROM FILM;
SELECT title AS judul_film,length AS durasi_film,rating
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length DESC
LIMIT 25;


# 5. Dari tabel “film”, tampilkan rating, Replacement Cost tertinggi, Rental Rate Terendah, dan Rata-Rata Durasi
# dan kelompokkan berdasarkan rating film!
SELECT * FROM FILM;
SELECT rating,
	MAX(replacement_cost) AS biaya_penggantian_tertinggi,
    MIN(rental_rate) AS tarif_rental_terendah,
    ROUND(AVG(length), 2) AS rata_rata_durasi_film
FROM film
GROUP BY rating
ORDER BY rating;


# 6. Tampilkan 15 daftar film yang memiliki huruf “K” pada akhir pada title, lalu tampilkan title, durasi,
# serta Bahasa pada film!
# Sebagai catatan, lakukan join terlebih dahulu dari tabel “film” dan tabel “language”!
SELECT * FROM film;

SELECT f.title AS judul_film,f.length AS durasi_film,l.name AS bahasa
FROM film f
JOIN language l ON f.language_id = l.language_id
WHERE f.title LIKE '%K'
LIMIT 15;

# 7. Tampilkan Judul Film (dari tabel “film”), First Name (dari tabel “actor”), dan Last Name (Dari tabel “actor”)
# dari actor yang memiliki “actor_id” = 14!
# Sebagai catatan, lakukan join table terlebih dahulu antara tabel “film”, “film_actor”, dan “actor”!
SELECT * FROM film;
SELECT * FROM actor;

SELECT f.title AS judul_film, a.first_name AS first_name, a.last_name AS last_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.actor_id = 14;


# 8. Dari tabel "city“, tampilkan city dan country id!
# Tampilkan hanya city atau kota yang namanya ada huruf "d" di posisi mana pun dan diakhiri huruf “a”!
# Tampilkan 15 data yang diurutkan berdasarkan city-nya secara ascending!
SELECT * FROM city;
SELECT city_id,city,country_id
FROM city
WHERE city LIKE '%d%a'
ORDER BY city ASC
LIMIT 15;


# 9. Tampilkan nama genre (name dari tabel “category”) dan jumlah banyaknya film di setiap genrenya!
# Lakukan join terlebih dahulu antara tabel “film”, “film_category”, dan “category”!
# Urutkan berdasarkan jumlah film di setiap kategorinya secara ascending!
SELECT * FROM category;
SELECT c.name AS genre_name, COUNT(f.film_id) AS film_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY film_count ASC;


# 10. Dari tabel “film”, tampilkan title, description, length, serta rating!
# Tampilkan 10 judul film yang diakhiri huruf ‘h’ dan durasinya di atas durasi rata-rata!
# Urutkan berdasarkan judulnya secara ascending!
SELECT * FROM film;

SELECT title,description,length, rating
FROM film
WHERE title LIKE '%h'AND length > (SELECT AVG(length) FROM film)
ORDER BY title ASC
LIMIT 10;

# =======================================================================================================================