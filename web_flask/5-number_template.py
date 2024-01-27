#!/usr/bin/python3
"""A script flask web application
listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return string
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbn():
    """Return string
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """followed by the value of the text variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def anot(text='is cool'):
    """python display the value of the text variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Disblay if n is number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """
        template path to display
    """
    return render_template('templates/5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
