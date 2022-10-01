from main import ma
from marshmallow.validate import Length

class TutorsSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["tutor_id", "first_name","last_name","email","password"]


    password = ma.String(validate=Length(8))
# Single tutor schema
tutor_schema = TutorsSchema()

#Mutliple tutor schema
tutors_schema = TutorsSchema(many=True)