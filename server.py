from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ekrgkesjrb'

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        file=request.files['myFile'] 
        file.save("static/"+"Image.jpeg")
        return render_template('show_id.html', form=form)
    else:
        return render_template('details.html', form=form)

app.run(debug=True)