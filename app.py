from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/MAct')
def MAct():
    return render_template('act.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(host="localhost", debug=True)