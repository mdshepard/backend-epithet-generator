
from flask import jsonify

from sprint_a import app


@app.route('/')
def generate_epithets():
    """Serves randomly generated witty banter"""
    return jsonify({"epithets": []})


@app.route('/vocabulary')
def vocabulary():
    """Serves the verbose components for said witty banter"""
    return jsonify({"vocabulary": {}})
