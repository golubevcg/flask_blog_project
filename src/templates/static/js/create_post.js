
let editor = new toastui.Editor({
    el: document.querySelector('#editor'),
    height: '500px',
    initialEditType: 'wysiwyg',
    previewStyle: 'vertical',
    theme: 'dark'
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

function send_and_save_post(header){

    if (!!!header) {
      alert("Error, given post header is empty!");
      return false;
    }

    let post_body = editor.getMarkdown();

    if (!!!post_body) {
      alert("Error, given post body is empty!");
      return false;
    }

    let post_data = {"header":header, "body":post_body}
    $.ajax({
        type: 'POST',
        url: '/create_new_post/save_new_post',
        data: JSON.stringify(post_data),
        headers: {"Content-Type": "application/json"},
        success: function(result){
            if (result !== ""){
                alert("New post successfully was saved!!");
                location.href = '/';
            } else {
                alert("There was an error during post saving!");
            }
        }
    })
}