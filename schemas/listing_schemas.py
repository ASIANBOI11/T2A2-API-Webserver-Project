from main import ma
from marshmallow import fields
from schemas.address_schemas import AddressSchema
from schemas.postcode_schemas import PostcodeSchema

class ListingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["listing_id", "price","description", "address_id", "address", "postcode_id", "postcode"]
        load_only = ["address_id"]

    #shows suburb, street name, street number and postcode
    address = fields.Nested("AddressSchema", only=("suburb", "street_name", "street_number","postcode"))

price = ma.Integer(required=True)
description = ma.String(required=True)

#single listing schema
listing_schema = ListingSchema()

#multiple listing schemas
listings_schema = ListingSchema(many=True)

