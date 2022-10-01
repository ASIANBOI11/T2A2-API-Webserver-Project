from pydoc import describe
from flask import Blueprint
from main import db
from main import bcrypt
from datetime import date
from models.tutors import Tutors
from models.subject import Subject
from models.students import Students

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
        email = "leo@gmail.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    db.session.add(tutor1)

    db.session.commit()

    student1 = Students(
        first_name = "Sarah",
        last_name = "Joey",
        email = "joe@example.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    student2 = Students(
        first_name = "Timmy",
        last_name = "Tom",
        email = "tom@example.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    db.session.add(student1)
    db.session.add(student2)

    db.session.commit()
    
    print("Tables seeded successfully")