from flask import Flask, request, jsonify, render_template, send_from_directory
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        result = subprocess.run(['python', temp_file_path], capture_output=True, text=True, timeout=5)
        output = result.stdout
        if result.stderr:
            output += f"\nError:\n{result.stderr}"
    except subprocess.TimeoutExpired:
        output = "Execution timed out"
    except Exception as e:
        output = f"An error occurred: {str(e)}"
    finally:
        os.unlink(temp_file_path)

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
