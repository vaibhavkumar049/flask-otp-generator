import random
import flask
from flask import Flask, render_template, url_for
from form import SimpleForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    generatedOTP= ''
    if flask.request.method == 'GET':
        generatedOTP = generate_random()
    if flask.request.method == 'POST':
        generatedOTP = ''

    return render_template('homepage.html', form=form, generatedOTP=generatedOTP)

def generate_random():
    return random.randint(10**9,10**10)

if(__name__ == '__main__'):
    app.run(debug=True)