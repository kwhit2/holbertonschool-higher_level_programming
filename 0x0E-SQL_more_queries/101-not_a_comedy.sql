-- script that lists all shows without the genre Comedy in the database...
-- ...hbtn_0d_tvshows.
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows;
FROM tv_show_genres;
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id;
ORDER BY number_shows DESC;
