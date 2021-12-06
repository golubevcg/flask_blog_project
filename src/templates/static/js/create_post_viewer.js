viewer_content = $('#viewer').text();

const viewer = toastui.Editor.factory({
  el: document.querySelector('#viewer'),
  viewer: true,
  height: '500px',
  initialValue: viewer_content,
});
