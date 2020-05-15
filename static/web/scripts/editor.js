ClassicEditor.create(document.querySelector('.editor'), {

    toolbar: {
        items: [
            'heading',
            '|',
            'bold',
            'italic',
            'link',
            'bulletedList',
            'numberedList',
            '|',
            'indent',
            'outdent',
            '|',
            'imageUpload',
            'blockQuote',
            'insertTable',
            'mediaEmbed',
            'undo',
            'redo',
            'codeBlock',
            'code',
            'highlight',
            'alignment'
        ]
    },
    language: 'en-gb',
    image: {
        toolbar: [
            'imageTextAlternative',
            'imageStyle:full',
            'imageStyle:side'
        ]
    },
    table: {
        contentToolbar: [
            'tableColumn',
            'tableRow',
            'mergeTableCells'
        ]
    },
    licenseKey: '',

}).then(editor => {
    window.editor = editor;
}).catch(error => {
    console.error('Oops, something gone wrong!');
    console.error('Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:');
    console.warn('Build id: ypjqgiv64z9o-andwo3judj4o');
    console.error(error);
});