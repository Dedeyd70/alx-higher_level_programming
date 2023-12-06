$(document).ready(function() {
      $("#btn_translate").click(function() {
        // Get the language code entered by the user
        let languageCode = $("#language_code").val();

        // Make an AJAX request to fetch the translation
        $.ajax({
          url: "https://www.fourtonfish.com/hellosalut/hello/",
          method: "GET",
          data: { lang: languageCode },
          success: function(data) {
            // Update the content of the <div> with the fetched translation
            $("#hello").text(data.hello);
          },
          error: function() {
            // Handle errors if the request fails
            $("#hello").text("Error: Failed to fetch translation");
          }
        });
      });
    });
