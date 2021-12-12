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
                let is_authenticated = $('meta[name=is_authenticated]').attr('content')
                let all_posts = result["all_posts"]
                let posts_years = result["post_years"]
                if (all_posts.length !== posts_years.length){
                    alert("Error! Post years amount does not fit all_posts amount!")
                }else{
                    let export_string = ""
                    for (let i = 0; i < all_posts.length; i++) {
                        let post = all_posts[i]
                        let is_alt = i % 2 === 0
                        export_string = export_string + create_post_div_from_post(post, is_authenticated, posts_years[i], is_alt)
                    }
                    // let scroll_position = $(document).pageYOffset ()
                    let scroll_position = $( "#container" ).scrollTop;
                    console.log("scroll_position:", scroll_position);
                    console.log("document.body.getBoundingClientRect().top\n:",document.body.getBoundingClientRect().top);
                    document.getElementById("posts-block").innerHTML = export_string;
                    change_pages_css(page_num)

                    if ( scroll_position !== null ) {
                        $(document).scrollTop( scroll_position );
                    }

                }
            }
          }
        })

    // query with ajax posts

    // iterate over this posts and create each post div

    // highlight current page with main color
    // set color to rest of the page numbers same bleak as other colors
}

function create_post_div_from_post(post, is_authenticated, post_years, is_alt){
    export_string = "<div class=\"text post-parent post_div\">"
                    + "<div class=\"text year\">"

    if (is_authenticated){
        export_string = export_string
                        + "<input class=\"btn btn-default text admin_button edit_button\" type=\"submit\" value=\"Edit\" onclick=\"edit_post(" + String(post.id) + ")\">"
                        + "<input class=\"btn btn-default text admin_button delete_button\" type=\"submit\" value=\"Delete\" onclick=\"delete_post(" + String(post.id) + ")\">"
    }else{
        export_string = export_string + post_years
    }
        export_string = export_string + "</div>"

    export_string = export_string + "<a class=\""
    if (is_alt){
        export_string = export_string + "post post-alt\""
    }else{
        export_string = export_string + "post\""
    }
    export_string = export_string + "href=\"post/" + String(post.id) + "\">"
                    + "<div class=\"text\" style=\"margin:8px\">" + post.header + "</div>"
                    + "<div style=\"flex-grow:1;\"></div>"
                    + "<div class=\"text\">" + post.creation_date + "</div>"
                    + "</a>"
                    + "</div>"

    return export_string
}

function change_pages_css(active_page){
    let page_divs = document.getElementsByClassName("pagination");
    for (page in page_divs){
        page.style = "color:red;"

    }
}