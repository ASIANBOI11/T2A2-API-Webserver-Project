from main import ma

class TutorsSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["tutor_id", "first_name","last_name","email"]


# Single tutor schema
tutor_schema = TutorsSchema()

#Mutliple tutor schema
tutors_schema = TutorsSchema(many=True)