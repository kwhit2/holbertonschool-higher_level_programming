-- script that lists all genres from hbtn_0d_tvshows and displays the number...
-- ...of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows;
FROM tv_show_genres;
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id;
ORDER BY number_shows DESC;
