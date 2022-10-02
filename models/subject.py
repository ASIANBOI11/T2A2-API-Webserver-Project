from main import db

class Subject(db.Model):
    #define the tablename of the database as subject
    __tablename__ = "subject"

    #Setting up columns
    subject_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String())
    description = db.Column(db.String())
    tutor = db.relationship(
        "Tutors",
        backref="subject",
    )