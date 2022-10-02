from main import ma
from marshmallow import fields

class PostcodeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["postcode_id", "postcode", "state"]

#single postcode schema
postcode_schema = PostcodeSchema()

#multiple postcodes schema
postcodes_schema = PostcodeSchema(many=True)