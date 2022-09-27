from main import db

class Tutors(db.Model):
    #define the tablename of the database as tutors
    __tablename__ ="tutors"

    #setting the columns
    tutor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    

    
