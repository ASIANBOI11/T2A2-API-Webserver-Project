from flask import Blueprint, jsonify, request
from main import db
from models.students import Students
from models.tutors import Tutors
from models.review import Review
from main import bcrypt
from main import jwt
from schemas.students_schemas import student_schema, students_schema
from schemas.review_schemas import review_schema, reviews_schema
from schemas.tutor_schemas import tutor_schema, tutors_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

students = Blueprint('students',__name__,url_prefix="/students")

@students.route("/", methods=["GET"])
@jwt_required()
def get_students():
    #Get all students from the database
    #Equals to the command SELECT * FROM STUDENT
    students_list = Students.query.all()
    result = students_schema.dump(students_list)
    return jsonify(result), 200

@students.route("/<int:id>", methods=["GET"])
# A token needed for this request
@jwt_required()
def get_student(id):
    # Get the student from the database by id
    student = Students.query.get(id)
    result = students_schema.dump(student)
    if not student:
        return {"error": "Student not found"}, 404
    return jsonify(result), 200

@students.route("/", methods=["POST"])
# A token needed for this request
@jwt_required()
def new_tutor():
    # Get the student field information from the student_schema
    student_fields = student_schema.load(request.json)
    student = Students(
        first_name = student_fields["first_name"],
        last_name = student_fields["last_name"],
        email = student_fields["email"],
        password = bcrypt.generate_password_hash(student_fields["password"]).decode("utf-8")
    )
    # Add the the database
    db.session.add(student)
    # Commit to the database
    db.session.commit()
    return jsonify(student_schema.dump(student)), 201

@students.route("/<int:id>", methods=["PUT"])
# A token needed for this request
@jwt_required()
def update_student(id):
    # Find the student from the database from id
    student = Students.query.get(id)

    if not student:
        return {"error": "Student not found"}, 404
    # Get student details
    student_fields = Students.load(request.json)

    student.first_name = student_fields["first_name"],
    student.last_name = student_fields["last_name"],
    student.email = student_fields["email"],
    # Commit the changes
    db.session.commit()

    return jsonify(student_schema.dump(student)), 201

@students.route("/<int:id>", methods=["DELETE"])
# A token needed for this request
@jwt_required()
def delete_student(id):
    #Find student in the database
    student = Students.query.get(id)

    if not student:
        return {"error": "Student not found"}, 404
    # Delete the student
    db.session.delete(student)

    db.session.commit()

    return {"message": "Student deleted successfully"}, 201


@students.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400
