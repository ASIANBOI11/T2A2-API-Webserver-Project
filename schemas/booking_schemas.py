from main import ma
from marshmallow import fields

class BookingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["booking_id","date", "tutor_id", "tutors", "student_id", "students"]


# Single booking schema
booking_schema = BookingSchema()

# Mutiple booking schema
bookings_schema = BookingSchema(many=True)