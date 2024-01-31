#!/usr/bin/python3
"""script Flask web application
script Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove SQLAlchemy Session
    after each request
    Remove SQLAlchemy Session
    after each request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """this for display a HTML page: inside the tag <BODY>
    tis for display a HTML page: inside the tag <BODY>
    <H1> tag: 'States'
    <UL> tag: 'List of all State objects present in DBStorage
    <LI> tag: description of one State
    <UL> tag: 'List of all State objects present in DBStorage
    <LI> tag: description of one State
    """
    states = sorted(storage.all(State).values(), key=lambda a: a.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
