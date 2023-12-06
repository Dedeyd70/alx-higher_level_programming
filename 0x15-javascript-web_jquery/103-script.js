 $(document).ready(function() {
      // Function to fetch and display translation
      function fetchTranslation() {
        const languageCode = $("#language_code").val();

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
      }

      // Trigger translation on button click
      $("#btn_translate").click(fetchTranslation);

      // Trigger translation on pressing ENTER in the input field
      $("#language_code").keypress(function(event) {
        if (event.which === 13) {
		fetchTranslation();
        }
      });
    });
