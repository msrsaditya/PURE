document.addEventListener('DOMContentLoaded', () => {
    const editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
        mode: 'python',
        theme: 'monokai',
        lineNumbers: true,
        autoCloseBrackets: true,
        matchBrackets: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        lineWrapping: true,
        extraKeys: {
            "Tab": "indentMore", 
            "Shift-Tab": "indentLess",
            "Cmd-Enter": runCode,
            "Ctrl-Enter": runCode,
            "Backspace": handleBackspace
        }
    });

    editor.setSize("100%", "100%");

    const output = document.getElementById('output');

    // Handle scrollbar visibility
    editor.on("scroll", function() {
        const vScroll = editor.getScrollerElement().querySelector('.CodeMirror-vscrollbar');
        if (vScroll) {
            vScroll.classList.add('active');
            setTimeout(() => vScroll.classList.remove('active'), 1000);
        }
    });

    function handleBackspace(cm) {
        const cursor = cm.getCursor();
        const line = cm.getLine(cursor.line);
        const lineBeforeCursor = line.slice(0, cursor.ch);
        
        if (/^\s+$/.test(lineBeforeCursor)) {
            const spaces = lineBeforeCursor.length;
            const indentUnit = cm.getOption("indentUnit");
            const dedentSize = spaces % indentUnit || indentUnit;
            
            cm.replaceRange("", 
                {line: cursor.line, ch: cursor.ch - dedentSize},
                {line: cursor.line, ch: cursor.ch},
                "+delete"
            );
            return;
        }
        
        CodeMirror.commands.delCharBefore(cm);
    }

    function runCode() {
        const code = editor.getValue();
        
        // Show loading animation
        output.innerHTML = '<div class="loading"></div>';

        fetch('/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code }),
        })
        .then(response => response.json())
        .then(data => {
            output.textContent = data.output + "\n\n========== Code Execution Successful ==========";
        })
        .catch(error => {
            console.error('Error:', error);
            output.textContent = 'An error occurred while running the code.';
        });
    }
});
