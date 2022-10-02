from main import db
from datetime import date

class Booking(db.Model):
    __tablename__ = "booking"

    booking_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"))
    tutor_id = db.Column(db.Integer, db.ForeignKey("tutors.tutor_id"))

