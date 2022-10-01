from main import db

class Listing(db.Model):
    #define the tablename of the database as review
    __tablename__ ="listing"

    #setting the columns
    listing_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float())
    description = db.Column(db.String())
