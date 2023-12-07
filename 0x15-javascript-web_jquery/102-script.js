$(document).ready(function() {
      $("#btn_translate").click(function() {
       
        let languageCode = $("#language_code").val();

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
      });
    });
