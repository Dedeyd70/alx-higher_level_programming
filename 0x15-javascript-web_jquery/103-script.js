 $(document).ready(function() {
      // Function to fetch and display translation
      function fetchTranslation() {
        const languageCode = $("#language_code").val();

        $.ajax({
          url: "https://hellosalut.stefanbohacek.dev/?",
          method: "GET",
          data: { lang: languageCode },
          success: function(data) {

            $("#hello").text(data.hello);
          },
          error: function() {
           
            $("#hello").text("Error: Failed to fetch translation");
          }
        });
      }

      // Trigger translation on button click
      $("#btn_translate").click(fetchTranslation);

           $("#language_code").keypress(function(event) {
        if (event.which === 13) {
		fetchTranslation();
        }
      });
    });
