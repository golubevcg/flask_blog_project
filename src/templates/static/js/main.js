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

function edit_post(){

}

function delete_post(){

}