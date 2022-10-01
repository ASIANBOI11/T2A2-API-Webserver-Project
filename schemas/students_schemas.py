from main import ma
from marshmallow.validate import Length

class StudentsSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["student_id", "first_name","last_name","email","password"]


    password = ma.String(validate=Length(8))
#single student schema
student_schema = StudentsSchema()

#multiple student schemas
students_schema = StudentsSchema(many=True)

