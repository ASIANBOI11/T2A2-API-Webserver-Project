from main import ma
from marshmallow import fields
from schemas.postcode_schemas import PostcodeSchema

class AddressSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["address_id", "suburb", "street_name", "street_number", "postcode_id", "postcode"]
        load_only = ["postcode_id"]

    postcode = fields.Nested("PostcodeSchema", only=("postcode", "state"))


# single address schema
address_schema = AddressSchema()

#mutliple address schema
addresses_schema = AddressSchema(many=True)