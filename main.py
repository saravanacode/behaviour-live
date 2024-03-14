from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
csrf = CSRFProtect(app)

class UploadFileForm(FlaskForm):
    file = FileField("File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = "inputvideo"  # Fixed filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File has been uploaded."
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

