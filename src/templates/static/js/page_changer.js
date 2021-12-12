function change_post_page(page_num){
    if(!!!page_num){
      alert("Error, given page number is empty!");
      return false;
    }

    // remove posts
    const elements = document.getElementsByClassName("post_div");
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }

      $.ajax({
          type: 'POST',
          url: '/get_posts_from_page_num/' + String(page_num),
          success: function(result){
            if (result==="") {
                alert("There was an error during loading page posts!");
            }else{
                result = JSON.parse(result)

                let all_posts = result["all_posts"]
                let post_years = result["post_years"]
                let pages_amount = result["pages_amount"]

                for (let i = 0; i < all_posts.length; i++) {

                }
            }
          }
        })

    // query with ajax posts

    // iterate over this posts and create each post div

    // highlight current page with main color
    // set color to rest of the page numbers same bleak as other colors
}

function create_posts_in_page(posts_list){

}

function change_pages_css(active_page){

}