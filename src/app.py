"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
#Get
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }

    return jsonify(response_body), 200

#Agregar Post
@app.route('/member', methods=['POST'])
def add_member():  
    request_body = request.json
    print(request_body)
    data = jackson_family.add_member(request_body)

    if data == True :
        return jsonify({"msg":"member created" }),200
    
    elif data != True:
        response = {"error": "Member not found"}
        return jsonify(response),400

 #Delete endpoint
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    members = jackson_family.delete_member(id)
    if not members :
        return jsonify({"msg":f"member with {id} does not exist"}),400
    return jsonify(members),200

#Get specifico 
@app.route('/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member= jackson_family.get_member(member_id)
    if member is None : 
        response = {"error": f"Member with ID {member_id} does not exist."}
        return jsonify(response),400
    return jsonify(member),200
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
