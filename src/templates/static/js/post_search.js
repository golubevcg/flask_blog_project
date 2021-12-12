$( document ).ready(function() {
    $("#input-search").keyup(function(event) {
        if (event.keyCode === 13) {
            let search_text = $("#input-search").val()
            if (search_text.length < 3 || search_text.length > 40) {
                alert("Search text can be only between 3 and 50 symbols, only words and no special characters.")
            }else{
                // ajax request for search w POST
                // update div post
            }


        }
    });
});
