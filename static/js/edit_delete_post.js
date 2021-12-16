function edit_post(post_id){
    location.href = '/create_new_post/' + String(post_id);
}

function delete_post(post_id){
  if (confirm("Are you sure, that you want to delete this post?")) {
      if (!!!post_id) {
          alert("Error, given post id is empty!");
          return false;
      }

      $.ajax({
              type: 'POST',
              url: '/post/delete_post/' + String(post_id),
              success: function(result){
                if (result==="") {
                    alert("There was an error during post deletion!");
                }else{
                    alert("Post was successfully deleted!");
                    location.href = '/';
                }
              }
            })
  } else {
  }
}
