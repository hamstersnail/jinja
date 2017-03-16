from flask import Flask, request, render_template
from random import choice, randint


app = Flask(__name__)

COMPLIMENTS = ["fine", "great", "suitable", "creative"]

@app.route('/')
def index():
    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    return "<html><body><h1>Hello</h1></body></html>"


@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky_number.html', lucky_num=num)


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/greet')
def offer_greeting():
    person = request.args.get('dude')
    nice_thing = choice(COMPLIMENTS)
    return render_template('compliment.html', name=person, compliment=nice_thing)


if __name__ == "__main__":
    app.run(debug=True)
