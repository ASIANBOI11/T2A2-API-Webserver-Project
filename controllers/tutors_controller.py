from flask import Blueprint, jsonify, request
from main import db
from models.tutors import Tutors
from main import bcrypt
from main import jwt
from schemas.tutor_schemas import tutor_schema, tutors_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

tutors = Blueprint('tutors', __name__, url_prefix="/tutors")

@tutors.route("/", methods=["GET"])
@jwt_required()
def get_tutors():
    # Get all tutors from the database 
    # Equals to the command SELECT * FROM TUTORS
    tutors_list = Tutors.query.all()
    result = tutors_schema.dump(tutors_list)
    return jsonify(result)

@tutors.route("/<int:id>", methods=["GET"])
# A token needed for this request
@jwt_required()
def get_tutor(id):
    tutor = Tutors.query.get(id)
    result = tutor_schema.dump(tutor)

    if not tutor:
        return {"error": "No tutors found"}, 404

    return jsonify(result)

@tutors.route("/", methods=["POST"])
# A token needed for this request
@jwt_required()
def new_tutor():
    # Load the tutor fields
    tutor_fields = tutor_schema.load(request.json)
    tutor = Tutors(
        first_name = tutor_fields["first_name"],
        last_name = tutor_fields["last_name"],
        email = tutor_fields["email"],
        password = bcrypt.generate_password_hash(tutor_fields["password"]).decode("utf-8"),

    )

    db.session.add(tutor)
    db.session.commit()
    return jsonify(tutor_schema.dump(tutor)), 201


@tutors.route("/<int:id>", methods=["PUT"])
# A token needed for this request
@jwt_required()
def update_tutor(id):
    #Find tutor in the database
    tutor = Tutors.query.get(id)

    if not tutor:
        return {"error": "No tutor found"}

    tutor_fields = Tutors.load(request.json)

    tutor.first_name = tutor_fields["first_name"]
    tutor.last_name = tutor_fields["last_name"]
    tutor.email = tutor_fields["email"]

    db.session.commit()

    return jsonify(tutor_schema.dump(tutor)), 201

# Delet the tutor from the database
tutors.route("/<int:id>", methods=["DELETE"])
# A token needed for this request
def delete_tutor(id):
    #Find tutor in the database
    tutor = Tutors.query.get(id)

    if not tutor:
        return {"error": "No tutor found"}

    db.session.delete(tutor)

    db.session.commit()

    return {"message": "Deleted Tutor successfully"}, 201

@tutors.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400
