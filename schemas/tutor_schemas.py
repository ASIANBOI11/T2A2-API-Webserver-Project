from main import ma
from marshmallow.validate import Length
from marshmallow import fields
from schemas.subject_schemas import SubjectSchema
from schemas.listing_schemas import ListingSchema
from schemas.address_schemas import AddressSchema

class TutorsSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["tutor_id", "first_name","last_name","email","password", "subject_id", "subject", "listing_id", "listing", "address_id", "address", "address_id"]
        load_only = ["subject_id", "listing_id"]


    subject = fields.Nested("SubjectSchema", only=("subject","description"))
    listing = fields.Nested("ListingSchema", only=("price","description","address"))

    first_name = ma.String(required=True)
    last_name = ma.String(required=True)
    email = ma.String(required=True)

    password = ma.String(validate=Length(8))
# Single tutor schema
tutor_schema = TutorsSchema()

#Mutliple tutor schema
tutors_schema = TutorsSchema(many=True)