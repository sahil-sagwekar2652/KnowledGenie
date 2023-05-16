import backend
from flask import Flask, render_template, request, session, redirect, url_for, jsonify  # noqa: E501
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template(template_name_or_list='index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        file_path = os.path.join('', uploaded_file.filename)
        print("\n\n", file_path, "\n\n")
        uploaded_file.save(file_path)
        session['file_path'] = file_path
        return redirect(url_for('process'))


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        query = request.json['query']

        if 'file_path' in session:
            file_path = session['file_path']

            # Running the model from backend\script.py
            # This code loads a model from the HuggingFace repository.
            qa_model = backend.main(file_path)
            result = qa_model(query)
            answer = result['result']
            # source = result['source_documents'][0].metadata['source']

            # os.remove(file_path)
            # session.pop('file_path', None)
            return jsonify({'answer': answer})
        else:
            return 'No file uploaded.'
    elif request.method == 'GET':
        return render_template('chat.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 3000), debug=True)
