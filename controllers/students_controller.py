from flask import Blueprint, jsonify, request
from main import db
from models.students import Students
from models.review import Review
from main import bcrypt
from main import jwt
from schemas.students_schemas import student_schema, students_schema
from schemas.review_schemas import review_schema, reviews_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

students = Blueprint('students',__name__,url_prefix="/students")

@students.route("/", methods=["GET"])

def get_students():
    #Get all students from the database
    #Equals to the command SELECT * FROM STUDENT
    students_list = Students.query.all()
    result = students_schema.dump(students_list)
    return jsonify(result)

@students.route("/<int:id>", methods=["GET"])
def get_student(id):
    student = Students.query.get(id)
    result = students_schema.dump(student)

    if not student:
        return {"error": "Student not found"}
    return jsonify(result)

@students.route("/", methods=["POST"])
def new_tutor():
    student_fields = student_schema.load(request.json)
    student = Students(
        first_name = student_fields["first_name"],
        last_name = student_fields["last_name"],
        email = student_fields["email"],
        password = bcrypt.generate_password_hash(student_fields["password"]).decode("utf-8")
    )

    db.session.add(student)
    db.session.commit()
    return jsonify(student_schema.dump(student))

@students.route("/<int:id>", methods=["PUT"])
def update_student(id):
    student = Students.query.get(id)

    if not student:
        return {"error": "Student not found"}

    student_fields = Students.load(request.json)

    student.first_name = student_fields["first_name"],
    student.last_name = student_fields["last_name"],
    student.email = student_fields["email"],

    db.session.commit()

    return jsonify(student_schema.dump(student))

@students.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    #Find student in the database
    student = Students.query.get(id)

    if not student:
        return {"error": "Student not found"}

    db.session.delete(student)

    db.session.commit()

    return {"message": "Student deleted successfully"}




