from main import db

class Postcode(db.Model):
    #define the tablename of the database as postcode
    __tablename__ = "postcode"

    #Setting the columns
    postcode_id = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.Integer(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    address = db.relationship(
        "Address",
        backref="postcode",
    )