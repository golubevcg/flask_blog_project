viewer_content = $('#viewer').text();

// const viewer = toastui.Editor.factory({
//   el: document.querySelector('#viewer'),
//   viewer: true,
//   height: '500px',
//   initialValue: viewer_content,
// });

let toolbarOptions = [
    [{ 'font': [] }],

    ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
    ['blockquote', 'code-block'],

    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'align': [] }],

    [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript

    [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
    [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

    [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme

    [ 'link', 'image', 'video', 'formula' ],

    ['clean']                                         // remove formatting button
];

hljs.configure({   // optionally configure hljs
  languages: ['python'],
});

let options = {
    debug: 'info',
    modules: {
        syntax: true,
        toolbar: toolbarOptions
    },
    readOnly: true,
    theme: 'bubble',
    tooltip:true,
};
let viewer = new Quill(document.querySelector('#viewer'), options);
viewer.setContents(JSON.parse(viewer_content))