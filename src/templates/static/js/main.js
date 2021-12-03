const Editor = toastui.Editor;
viewer_content = $('#viewer').text();

const viewer = Editor.factory({
  el: document.querySelector('#viewer'),
  viewer: true,
  height: '500px',
  initialValue: viewer_content,
  theme: 'light'
});

function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-theme");
}
