from pydoc import describe
from re import sub
from flask import Blueprint
from main import db
from main import bcrypt
from models.tutors import Tutors
from models.subject import Subject
from models.students import Students
from models.review import Review
from models.listing import Listing
from models.postcode import Postcode
from models.address import Address
from models.booking import Booking

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

    subject1 = Subject(
        subject = "Math",
        description = "Teaches algebra and trigonometry",
    )

    db.session.add(subject1)
    db.session.commit()

    postcode1 = Postcode(
        postcode = 3000,
        state = "New South Wales"
    )

    db.session.add(postcode1)
    db.session.commit()
    

    address1 = Address(
        suburb = "Lavington",
        street_name = "Numberjack",
        street_number = 22,
        postcode_id = postcode1.postcode_id
    )

    db.session.add(address1)
    db.session.commit()


    listing1 = Listing(
        price = 30,
        description = "This is leo, I teach math and programming",
        address_id = address1.address_id,
    )

    db.session.add(listing1)
    db.session.commit()

    tutor1 = Tutors(
        first_name = "Leo",
        last_name = "Pen",
        email = "leo@gmail.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8"),
        subject_id = subject1.subject_id,
        listing_id = listing1.listing_id

    )

    db.session.add(tutor1)
    db.session.commit()
    
    student1 = Students(
        first_name = "Sarah",
        last_name = "Joey",
        email = "joe@example.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    db.session.add(student1)


    student2 = Students(
        first_name = "Timmy",
        last_name = "Tom",
        email = "tom@example.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    db.session.add(student2)

    db.session.commit()
    
    print("Tables seeded successfully")