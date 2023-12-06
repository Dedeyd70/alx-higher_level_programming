$.ajax({
      url: "https://swapi-api.alx-tools.com/api/films/?format=json",
      method: "GET",
      success: function(data) {
        // Iterate through each movie and append its title to the <ul>
        $.each(data.results, function(index, movie) {
          $("#list_movies").append("<li>" + movie.title + "</li>");
        });
      },
      error: function() {
        // Handle errors if the request fails
        $("#list_movies").append("<li>Error: Failed to fetch movie titles</li>");
      }
    });
