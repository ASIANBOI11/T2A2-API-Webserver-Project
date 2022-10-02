from datetime import timedelta
from flask import Blueprint, jsonify, request
from main import db
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token
from models.tutors import Tutors
from models.students import Students
from schemas.students_schemas import student_schema
from schemas.tutor_schemas import tutor_schema
from marshmallow.exceptions import ValidationError

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route('/register/student', methods=['POST'])
def register_student():
    #get details from the request
    student_fields = student_schema.load(request.json)
    # Check the student email if the student email already exist in the database
    student = Students.query.filter_by(email=student_fields["email"]).first()
    if student:
        return {"error": "Email already registered"}, 400
    #Create user object
    student = Students(
        first_name = student_fields["first_name"],
        last_name = student_fields["last_name"],
        email = student_fields["email"],
        password = bcrypt.generate_password_hash(student_fields["password"]).decode("utf-8")
    )

    # Add the student to the database
    db.session.add(student)
    # Save the changes to the database
    db.session.commit()
    # Generate a token that is the identity of the student. Expires in one day
    token = create_access_token(identity=str(student.student_id), expires_delta=timedelta(days=1))

    return {"firstname" : student.first_name,"access_token": student.email, "token": token}, 201

# Login student post request
@auth.route('/student/login', methods=['POST'])
def student_login():
    # Get the email and password from the request
    student_fields = student_schema.load(request.json)
    # Check the email and password. Email needs to exist, and the password matches
    student = Students.query.filter_by(email=student_fields["email"]).first()
    if not student:
        return {"error": "Email not registered"}, 404
    
    if not bcrypt.check_password_hash(student.password, student_fields["password"]):
        return {"error": "Password not correct"}, 401
    # Generate a token that is the identity of the student. Expires in one day
    token = create_access_token(identity=str(student.student_id),expires_delta=timedelta(days=1))
    # Login successfully, information was correct
    return {"email": student.email, "token": token}
    

@auth.route('/register/tutor', methods=['POST'])
def register_tutor():
    #get details from the request
    tutor_fields = tutor_schema.load(request.json)
    #Check the Email if it already exist in the database
    tutor = Tutors.query.filter_by(email=tutor_fields["email"]).first()
    if tutor:
        return {"error": "Email already registered"}, 400
    #Create user object
    tutor = Tutors(
        first_name = tutor_fields["first_name"],
        last_name = tutor_fields["last_name"],
        email = tutor_fields["email"],
        password = bcrypt.generate_password_hash(tutor_fields["password"]).decode("utf-8"),
    )

    # Add the student to the database
    db.session.add(tutor)
    # Save the changes to the database
    db.session.commit()
    # Generate a token that is the identity of the student. Expires in one day
    token = create_access_token(identity=str(tutor.tutor_id), expires_delta=timedelta(days=1))
    # Login successfully, information was correct
    return {"access_token": tutor.email, "token": token}

@auth.route('/tutor/login', methods=['POST'])
def tutor_login():
    # Get the email and password from the request
    tutor_fields = tutor_schema.load(request.json)
    # Check the email and password. Email needs to exist, and the password matches
    tutor = Tutors.query.filter_by(email=tutor_fields["email"]).first()
    if not tutor:
        return {"error": "Email not registered"}, 404
    
    if not bcrypt.check_password_hash(tutor.password, tutor_fields["password"]):
        return {"error": "Password not correct"}, 401
    # Generate a token that is the identity of the student. Expires in one day
    token = create_access_token(identity=str(tutor.tutor_id),expires_delta=timedelta(days=1))
    # Login successfully, information was correct
    return {"email": tutor.email, "token": token}
    

# ValidationError
@auth.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400

