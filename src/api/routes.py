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
    return jsonify(todos) , 200

@api.route('/todos', methods=['POST'])
def post_todos():
    
    payload = request.json
    todos.append(payload[("title")])

    return jsonify(todos), 200

@api.route('/todos/<int:position>', methods=['DELETE'])
def delete_todos(position):
    global todos
    
    if len(todos) < position:
            return "Position does not matach", 400
    else:
        todos.pop(position)
        
        return jsonify(todos), 200