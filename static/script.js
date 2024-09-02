document.addEventListener('DOMContentLoaded', () => {
    const editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
        mode: 'python',
        theme: 'monokai',
        lineNumbers: true,
        autoCloseBrackets: true,
        matchBrackets: true,
        autoCloseTags: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        extraKeys: {
            "Tab": "indentMore", 
            "Shift-Tab": "indentLess",
            "Ctrl-Space": "autocomplete",
            "Cmd-Enter": runCode,
            "Ctrl-Enter": runCode  // For non-Mac users
        }
    });

    // Ensure the editor fills its container
    editor.setSize("100%", "100%");

    const output = document.getElementById('output');

    function runCode() {
        const code = editor.getValue();
        
        fetch('/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code }),
        })
        .then(response => response.json())
        .then(data => {
            output.textContent = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
            output.textContent = 'An error occurred while running the code.';
        });
    }
});
