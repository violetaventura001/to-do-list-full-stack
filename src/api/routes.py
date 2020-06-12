"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
#from models import Person

api = Blueprint('api', __name__)

todos =[]

@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@api.route('/todos', methods=['POST'])
def post_todos():
    payload = request.json
    return jsonify(payload)

@api.route('/todos', methods=['DELETE'])
def delete_todos():
    return jsonify(todos), 200