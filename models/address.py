from main import db

class Address(db.Model):
    #define the tablename of the database as review
    __tablename__ ="address"

    #setting the columns
    address_id = db.Column(db.Integer, primary_key=True)
    suburb = db.Column(db.String())
    street_name = db.Column(db.String())
    street_number = db.Column(db.String())
