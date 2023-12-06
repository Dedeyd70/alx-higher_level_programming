 $(document).ready(function() {
      $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        method: "GET",
        success: function(data) {
          // Update the text content of the <div> with the fetched translation
          $("#hello").text(data.hello);
        },
        error: function() {
          // Handle errors if the request fails
          $("#hello").text("Error: Failed to fetch translation");
        }
      });
    });
