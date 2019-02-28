
from flask import jsonify
from sprintb import app
from sprintb.helpers import Vocabulary as vernacular
from sprintb.helpers import EpithetGenerator

path = '../../resources/data.json'


@app.route('/')
@app.route("/epithets/<int:quantity>")
def generate_epithets(quantity=1):
    """Serves randomly generated witty banter"""
    return jsonify(EpithetGenerator.generate_epithets(
        path, quantity)
        )


@app.route('/random')
def random_num_epithets():
    """serves a random number of abusive phrases"""
    return jsonify(EpithetGenerator.random_num_epithets(
            path)
        )


@app.route('/vocabulary')
def vocabulary():
    """Serves the verbose components for said witty banter"""
    full_vocabulary = vernacular.from_file(path)[0]
    return jsonify(full_vocabulary)
