from main import db

class Review(db.Model):
    #define the tablename of the database as review
    __tablename__ ="review"

    #setting the columns
    review_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer())
    description = db.Column(db.String())