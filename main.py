from flask import Flask, render_template, request
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
    file = request.files['file']
    filename = file.filename

    if not os.path.exists('uploads'):
        os.mkdir('uploads')

    file.save(os.path.join('uploads', filename))
    return "<h3>File Uploaded Successfully</h3>"
    # return redirect(location=url_for(endpoint='index'))


if __name__ == '__main__':
    app.run(debug=True)
