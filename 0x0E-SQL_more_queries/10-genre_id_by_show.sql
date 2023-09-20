-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
SELECT tvs.title, tvsg.genre_id
  FROM tv_shows AS tvs
        INNER JOIN tv_show_genres AS tvsg
	ON tvs.id = tvsg.show_id
 ORDER BY tvs.title,tvsg.genre_id;
