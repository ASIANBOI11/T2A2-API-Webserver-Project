from main import ma
from marshmallow.validate import Length
from marshmallow import fields
from schemas.review_schemas import ReviewSchema

class StudentsSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["student_id", "first_name","last_name","email","password", "review_id", "review"]
        load_only = ["review_id"]

    subject = fields.Nested(ReviewSchema, only=("rating","description"))

    first_name = ma.String(required=True)
    last_name = ma.String(required=True)
    email = ma.String(required=True)


    password = ma.String(validate=Length(8))
#single student schema
student_schema = StudentsSchema()

#multiple student schemas
students_schema = StudentsSchema(many=True)

