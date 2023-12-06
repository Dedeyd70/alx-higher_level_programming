$.ajax({
      url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
      method: "GET",
      success: function(data) {
        // Update the text content of the <div> with the fetched character name
        $("#character").text(data.name);
      },
      error: function() {
        // Handle errors if the request fails
        $("#character").text("Failed to fetch character name");
      }
    });
