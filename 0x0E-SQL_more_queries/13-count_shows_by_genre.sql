-- Lists all genres from the database hbtn_0d_tvshows
SELECT tvg.name AS genre,
       COUNT(*) AS number_of_shows
  FROM tv_genres AS tvg
       INNER JOIN tv_show_genres AS tvsg
       ON tvg.id = tvsg.genre_id
 GROUP BY tvg.name
 ORDER BY number_of_shows DESC;
