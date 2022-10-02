from flask import Blueprint, jsonify, request
from main import db
from models.tutors import Tutors
from main import bcrypt
from main import jwt
from schemas.tutor_schemas import tutor_schema, tutors_schema

tutors = Blueprint('tutors', __name__, url_prefix="/tutors")

@tutors.route("/", methods=["GET"])
def get_tutors():
    # Get all tutors from the database 
    # Equals to the command SELECT * FROM TUTORS
    tutors_list = Tutors.query.all()
    result = tutors_schema.dump(tutors_list)
    return jsonify(result)

@tutors.route("/<int:id>", methods=["GET"])
def get_tutor(id):
    tutor = Tutors.query.get(id)
    result = tutor_schema.dump(tutor)

    if not tutor:
        return {"error": "No tutors found"}

    return jsonify(result)

@tutors.route("/", methods=["POST"])
def new_tutor():
    tutor_fields = tutor_schema.load(request.json)
    tutor = Tutors(
        first_name = tutor_fields["first_name"],
        last_name = tutor_fields["last_name"],
        email = tutor_fields["email"],
        password = bcrypt.generate_password_hash(tutor_fields["password"]).decode("utf-8"),

    )

    db.session.add(tutor)
    db.session.commit()
    return jsonify(tutor_schema.dump(tutor))


@tutors.route("/<int:id>", methods=["PUT"])
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

    return jsonify(tutor_schema.dump(tutor))

# Delet the tutor from the database
tutors.route("/<int:id>", methods=["DELETE"])
def delete_tutor(id):
    #Find tutor in the database
    tutor = Tutors.query.get(id)

    if not tutor:
        return {"error": "No tutor found"}

    db.session.delete(tutor)

    db.session.commit()

    return {"message": "Deleted Tutor successfully"}
