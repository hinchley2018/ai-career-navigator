from flask import Blueprint, jsonify
from app.extensions import mongo

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/items', methods=['GET'])
def get_items():
    items = mongo.db.items.find()
    return jsonify([item for item in items])
