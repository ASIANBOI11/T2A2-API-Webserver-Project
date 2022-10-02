from flask import Blueprint, jsonify, request
from main import db
from main import bcrypt
from main import jwt
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import Booking
from models.tutors import Tutors
from models.students import Students
from schemas.booking_schemas import booking_schema, bookings_schema

booking = Blueprint('booking', __name__, url_prefix="/booking")

#Get all the bookings
@booking.route("/", methods=['GET'])
def get_all_bookings():

    #Find the bookings in the database
    bookings_list = Booking.query.all()
    result = bookings_schema.dump(bookings_list)
    return jsonify(result)


# Students can book the tutor for their teaching
@booking.route("/<int:student_id>/booking/<int:tutor_id>", methods=["POST"])
def new_booking(student_id, tutor_id):
    # Find the student in the database
    student = Students.query.get(student_id)
    # Check if the student exist in the database
    if not student:
        return {"error": "Student not found in the database"}
    # Find the tutor in the database
    tutor = Tutors.query.get(tutor_id)
    # Check if the tutor exist in the database
    if not tutor:
        return {"error": "Tutor not found in the database"}
   
    
    booking = Booking(
        student = student,
        tutor = tutor,
        date = date.today()
        )

    db.session.add(booking)
    db.session.commit()
    return jsonify(booking_schema.dump(booking))
    



