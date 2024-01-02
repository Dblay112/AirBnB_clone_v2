#!/usr/bin/python3
"""a script that starts a Flask web application:

Your web application must be on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_hbnb(text):
    """display text"""
    rep_text = text.replace('_', ' ')
    return "C {}".format(rep_text)


@app.route("/python/<text>", strict_slashes=False)
@app.route('/python/', defaults={"text": 'is cool'}, strict_slashes=False)
def p_text(text):
    """python text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def n_number(n):
    """n is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(text):
    """Displays an HTML page only if <n> is an integer"""
    return render_template('5-number_template.html', number=n)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
