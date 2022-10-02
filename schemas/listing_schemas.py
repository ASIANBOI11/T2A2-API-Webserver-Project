from main import ma
from marshmallow import fields
from schemas.address_schemas import AddressSchema
from schemas.postcode_schemas import PostcodeSchema

class ListingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["listing_id", "price","description", "address_id", "address", "postcode_id", "postcode"]
        load_only = ["address_id"]

    address = fields.Nested("AddressSchema", only=("suburb", "street_name", "street_number","postcode"))


#single listing schema
listing_schema = ListingSchema()

#multiple listing schemas
listings_schema = ListingSchema(many=True)

