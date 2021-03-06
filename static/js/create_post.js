
$(document).ready(function() {
    let post_body = $('#editor').text();
    $('#editor').empty();

    if (!!!post_body){
        $('#editor').summernote({
            dialogsInBody: true,
            fontName: ['JetBrains Mono']
        });
        $('#editor').summernote('color', "var(--text_main_color)");
    }else{
        $('#editor').summernote({
            dialogsInBody: true,
            fontName: ['JetBrains Mono'],
        });
        $('#editor').summernote('editor.pasteHTML', post_body);
        $('#editor').summernote('color', "var(--text_main_color)");
    }

});

function save_post(){
    let header = $('#post_header_input').val();
    validate_header(header)
}

function validate_header(header){
    if (!!!header) {
      alert("Error, given post header is empty!");
      return false;
    }

    if (header.length<5 || header.length>50) {
      alert("Error, header length must be between 5 and 50 symbols!");
      return false;
    }

    const queryString = window.location.pathname;
    let split = queryString.split("/")

    if (split.length > 2) {
        send_and_save_post(header)
    }else{
        $.ajax({
                type: 'POST',
                url: '/create_new_post/check_new_post_header_unique',
                data: JSON.stringify(header),
                headers: {"Content-Type": "application/json"},
                success: function(result){
                  if (!!result) {
                      send_and_save_post(header)
                  }else{
                      alert("Error, given post header already exists in database, please provide unique header!");
                      return false;
                  }
                }
              })
    }
}

function send_and_save_post(header){

    if (!!!header) {
      alert("Error, given post header is empty!");
      return false;
    }

    let post_body = $('#editor').summernote('code');
    console.log("type(post_body)=", typeof(post_body))
    let is_published = $('#publish_checkbox').prop('checked')
    let is_link_access = $('#link_access_checkbox').prop('checked')
    let is_deleted = $('#is_deleted').prop('checked')

    if (!!!post_body) {
      alert("Error, given post body is empty!");
      return false;
    }

    if (confirm("Are you sure, that you want to save this post?")) {
        const queryString = window.location.pathname;
        let split = queryString.split("/")
        let post_id = null
        if (split.length > 2){
            post_id = split[2]
        }

        let post_data = {
            "header": header,
            "body": post_body,
            "is_published": is_published,
            "is_link_access": is_link_access,
            "is_deleted": is_deleted
        }
        if (!!post_id){
            post_id = parseInt(post_id)
            $.ajax({
                    type: 'POST',
                    url: '/create_new_post/check_post_with_this_id_exists',
                    data: JSON.stringify(post_id),
                    headers: {"Content-Type": "application/json"},
                    success: function(result){
                      if (!!result) {
                            post_data["post_id"] = post_id
                            send_post_data(post_data)
                      }else{
                          alert("Error, cannot update post, post with such id does not exist!");
                          return false;
                      }
                    }
                  })
        } else{
            send_post_data(post_data)
        }
    }
}

function send_post_data(post_data){
    if (!!post_data){
        $.ajax({
            type: 'POST',
            url: '/create_new_post/save_new_post',
            data: JSON.stringify(post_data),
            headers: {"Content-Type": "application/json"},
            success: function (result) {
                if (result !== "") {
                    alert("New post successfully was saved!!");
                    location.href = '/';
                } else {
                    alert("There was an error during post saving!");
                }
            }
        })
    }
}
