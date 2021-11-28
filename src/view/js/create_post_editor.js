window.addEventListener('load', function() {

  const Editor = toastui.Editor;

  const editor = new Editor({
    el: document.querySelector('#editor'),
    height: '500px',
    initialEditType: 'wysiwyg',
    previewStyle: 'vertical'
  });

  editor.getMarkdown();
});


