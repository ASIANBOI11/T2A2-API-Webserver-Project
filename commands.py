from pydoc import describe
from flask import Blueprint
from main import db
from models.tutors import Tutors
from models.subject import Subject

db_commands = Blueprint("db",__name__)

@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical DB
    db.create_all()
    print('Table creation')

@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables for all models in the physical DB
    db.drop_all()
    print('Table dropped')

@db_commands.cli.command('seed')
def seed_db():
    tutor1 = Tutors(
        first_name = "Leo",
        last_name = "Pen",
        email = "leo@gmail.com"
    )

    tutor2 = Tutors(
        first_name = "Alice",
        last_name = "Pen",
        email = "Alicepen@gmail.com"
    )

    db.session.add(tutor1)
    db.session.add(tutor2)

    subject1 = Subject(
        subject = "Math",
        description =  "The math subject teaches algebra, trigonomentry and probability"
    )
        
    db.session.add(subject1)

    db.session.commit()
    print("Tables seeded successfully")
