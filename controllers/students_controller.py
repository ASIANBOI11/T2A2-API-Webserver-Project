from flask import Blueprint, jsonify, request
from main import db
from models.students import Students
from schemas.students_schemas import student_schema, students_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

students = Blueprint('students',__name__,url_prefix="/students")

@students.route("/", methods=["GET"])
@jwt_required()
def get_students():
    #Get all students from the database
    #Equals to the command SELECT * FROM STUDENT
    students_list = Students.query.all()
    result = students_schema.dump(students_list)
    return jsonify(result)

