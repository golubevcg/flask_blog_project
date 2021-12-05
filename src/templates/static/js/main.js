const Editor = toastui.Editor;
viewer_content = $('#viewer').text();

const viewer = Editor.factory({
  el: document.querySelector('#viewer'),
  viewer: true,
  height: '500px',
  initialValue: viewer_content,
  theme: 'light'
});

function switch_theme() {
  var element = document.body;
  element.classList.toggle("dark-theme");
}

function edit_post(post_id){
  console.log(post_id)
}

function delete_post(post_id){
  console.log(post_id)
  if (confirm("Are you shure, that you want to delete this post?")) {
    // txt = "You pressed OK!";
  } else {
  }
}