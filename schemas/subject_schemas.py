from main import ma

class SubjectSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["subject_id", "subject" ,"description"]

    subject = ma.String(required=True)
    description = ma.String(required=True)

#Single tutor schema 
subject_schema = SubjectSchema()

#Multiple subject schema 
subjects_schema = SubjectSchema(many=True)

