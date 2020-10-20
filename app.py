import random
from flask import Flask, render_template, url_for
from form import SimpleForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    form = SimpleForm()
    return render_template('homepage.html', form=form)

def generate_random():
    return random.randint(0,9)

if(__name__ == '__main__'):
    app.run(debug=True)