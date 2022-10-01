from main import db

class Students(db.Model):
    #define the tablename of the database as students
    __tablename__ ="students"

    #setting the columns
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    
