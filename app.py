import random
import flask
from flask import Flask, render_template, url_for,request
from form import SimpleForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/",methods=['GET', 'POST'])
def test():
    form = SimpleForm()
    return render_template('homepage.html', form=form, generatedOTP=123)


@app.route('/te', methods=['GET', 'POST'])
def index():
    x=random.randint(10**9,10**10)
    if request.method=="GET":
        form = SimpleForm()
        print(x)
        return render_template('homepage.html', form=form, generatedOTP=x)
    else:
        data=int(request.form['otp'])
        prev=int(request.form['prev'])
        print(request.form)
        
        if data==prev:
            print(prev)
            print(data)
            return "correct" + " "+str(prev) +" "+str(data)
        else:
            print(data)
            print(prev)
            return "incorect"+ " "+str(prev) +" "+str(data)
        

def generate_random():
    return random.randint(10**9,10**10)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8888)