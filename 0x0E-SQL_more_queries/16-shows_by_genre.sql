-- Lists all shows and genres linked to the show from the database
SELECT tvs.title, tvg.name
  FROM tv_shows AS tvs
       LEFT JOIN tv_show_genres AS tvsg
       ON tvs.id = tvsg.show_id

       LEFT JOIN tv_genres AS tvg
       ON tvsg.genre_id = tvg.id
 ORDER BY tvs.title, tvg.name;
