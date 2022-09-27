from flask import Blueprint, jsonify
from main import db
from models.subject import Subject
from schemas.subject_schemas import subject_schema, subjects_schema

subject = Blueprint('subject', __name__, url_prefix="/subject")

@subject.route("/", methods=["GET"])
def get_subject():
    subject_list = Subject.query.all()
    result = subjects_schema.dump(subject_list)
    return jsonify(result)

    