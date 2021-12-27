// let viewer_content = $('#viewer').text();
// $('#viewer').empty();
// viewer_content = JSON.parse(str)
// document.getElementById("viewer").innerHTML = viewer_content;



// $(document).ready(function() {
//     $('#viewer').summernote({
//         airMode: true,
//         dialogsInBody: true
//     });
//     $('#viewer').summernote('code', viewer_content);
// });
// .summernote('disable');

//
// let toolbarOptions = [
//     [{ 'font': [] }],
//
//     ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
//     ['blockquote', 'code-block'],
//
//     [{ 'list': 'ordered'}, { 'list': 'bullet' }],
//     [{ 'align': [] }],
//
//     [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
//
//     [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
//     [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
//
//     [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
//
//     [ 'link', 'image', 'video', 'formula' ],
//
//     ['clean']                                         // remove formatting button
// ];
//
// hljs.configure({   // optionally configure hljs
//   languages: ['python'],
// });
//
// let options = {
//     debug: 'info',
//     modules: {
//         syntax: true,
//         toolbar: toolbarOptions
//     },
//     readOnly: true,
//     theme: 'bubble',
//     tooltip:true,
// };
// let viewer = new Quill(document.querySelector('#viewer'), options);
// viewer.setContents(JSON.parse(viewer_content))