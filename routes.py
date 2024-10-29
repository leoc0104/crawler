from flask import Flask, request, jsonify
from Controllers.EntityController import EntityController

app = Flask(__name__)
controller = EntityController()

@app.route('/entities', methods = ['POST'])
def create_entity():
    data = request.json

    return controller.store(data)

@app.route('/entities', methods = ['GET'])
def get_entities():
    return jsonify(controller.index())

@app.route('/entities/<id>', methods = ['GET'])
def get_entity(id):
    response, status_code = controller.show(id)
    
    return jsonify(response), status_code

@app.route('/entities/<id>', methods = ['PUT'])
def update_entity(id):
    new_values = request.get_json()
    
    response, status_code = controller.update(id, new_values)
    
    return jsonify(response), status_code

@app.route('/entities/<id>', methods = ['DELETE'])
def delete_entity(id):
    response, status_code = controller.destroy(id)
    
    return jsonify(response), status_code

@app.errorhandler(404)
def not_found(error = None):
    message = {
        'message': 'Route not found: ' + request.url,
        'status': 404
    }

    return jsonify(message), 404

if __name__ == "__main__":
    app.run(debug = True)
