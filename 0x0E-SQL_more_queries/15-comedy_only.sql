-- Lists all comedy shows in the database hbtn_0d_tvshows.
SELECT tvs.title
  FROM tv_shows AS tvs
       INNER JOIN tv_show_genres AS tvsg
       ON tvs.id = tvsg.show_id

       INNER JOIN tv_genres AS tvg
       ON tvg.id = tvsg.genre_id
       WHERE tvg.name = "Comedy"
 ORDER BY tvs.title;
