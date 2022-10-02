from main import ma
from marshmallow import fields
from marshmallow.validate import Length

class ReviewSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["review_id", "rating", "description" ]

    rating = ma.Integer(required=True)
    description = ma.String(required=True)
# Single review schema
review_schema = ReviewSchema()

#Mutiple review schema
reviews_schema = ReviewSchema(many=True)