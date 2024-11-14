# SAKILA
USE sakila;
SELECT * FROM film;
SELECT * FROM film_category;
SELECT * FROM category;

# 1. Tampilkan lima total rental_duration di tiap kategori film.
# Hitung jumlah kumulatif atau cumulative sum dan rata-rata bergerak atau moving average dari total rental_duration.
# Untuk membatasi data, pilih hanya film yang rental_duration-nya ≤ rata-rata keseluruhan rental_duration.

-- Cumulative sum --> SUM --> ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
-- Moving average --> AVG --> ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

WITH AvgRentalDuration AS (
    SELECT AVG(rental_duration) AS avg_rental_duration
    FROM film
),
CategoryRentalDuration AS (
    SELECT
        c.name AS category_name,
        SUM(f.rental_duration) AS total_rental_duration
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE f.rental_duration <= (SELECT avg_rental_duration FROM AvgRentalDuration)
    GROUP BY c.name
),
CumulativeAndMovingAverage AS (
    SELECT
        category_name,
        total_rental_duration,
        SUM(total_rental_duration) OVER (ORDER BY total_rental_duration DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_sum,
        AVG(total_rental_duration) OVER (ORDER BY total_rental_duration DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS moving_avg
    FROM
        CategoryRentalDuration
)

SELECT
    category_name AS name,
    total_rental_duration,
    cumulative_sum,
    moving_avg
FROM CumulativeAndMovingAverage
ORDER BY total_rental_duration DESC
LIMIT 5;


# 2. Tampilkan rating film beserta rata-rata durasi rentalnya.
# Gunakan data durasi rental film yang berasal dari 3 kategori dengan jumlah film terbanyak

SELECT * FROM film;

WITH TopCategories AS (
    SELECT
        c.category_id,
        c.name AS category_name,
        COUNT(fc.film_id) AS film_count
    FROM category c
    JOIN film_category fc ON c.category_id = fc.category_id
    GROUP BY c.category_id, c.name
    ORDER BY film_count DESC
    LIMIT 3
),
FilmsInTopCategories AS (
    SELECT
        f.film_id,
        f.rating,
        f.rental_duration
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN TopCategories tc ON fc.category_id = tc.category_id
),
RatingAverageDuration AS (
    SELECT
        rating,
        AVG(rental_duration) AS avg_rental_duration
    FROM FilmsInTopCategories
    GROUP BY rating
)

SELECT rating, avg_rental_duration
FROM RatingAverageDuration
ORDER BY avg_rental_duration DESC;


# 3. Tampilkan judul film dan total konsumen yang menyewa di tiap judul film tersebut.
# Saat menampilkan data tersebut, penuhi beberapa syarat berikut ini.
# Pertama, huruf pertama judul film adalah huruf ‘C’ atau ‘G’.
# Kedua, total konsumen yang menyewa di tiap judul film harus lebih tinggi dari rata-rata keseluruhan.
# Ketiga, total konsumen yang menyewa di tiap judul film harus ≥ 15 dan ≤ 25

# judul film --> title,
# total konsumen --> customer,


SELECT * FROM film;
SELECT * FROM customer;
SELECT * FROM film_category;
SELECT * FROM category;
SELECT * FROM inventory;


WITH FilmRentals AS (
    SELECT
        f.title,
        COUNT(r.rental_id) AS total_customers
    FROM film f
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    WHERE f.title LIKE 'C%' OR f.title LIKE 'G%'
    GROUP BY f.title
),
AverageRental AS (
    SELECT AVG(total_customers) AS avg_customers
    FROM FilmRentals
),
FilteredFilms AS (
    SELECT
        fr.title,
        fr.total_customers
    FROM FilmRentals fr
    JOIN AverageRental ar ON fr.total_customers > ar.avg_customers
    WHERE fr.total_customers BETWEEN 15 AND 25
)

SELECT title,total_customers
FROM FilteredFilms
ORDER BY title;