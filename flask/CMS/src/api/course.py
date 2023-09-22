import datetime
from flask import Blueprint, jsonify, abort, request
from ..models import User_Account, Student, Course, Professor, cp_table, db

bp = Blueprint('courses', __name__, url_prefix='/courses')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    c = Course.query.all() # ORM performs SELECT query
    result = []
    for i in c:
        result.append(i.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

#retrieves selected course by id number
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Course.query.get_or_404(id, "Course not found")
    return jsonify(c.serialize())

#creates a new course row
@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json or 'start_date' not in request.json or 'end_date' not in request.json:
        return abort(400)
    elif len(request.json['name']) < 3:
        return abort(400)
    c = Course(
        name=request.json['name'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date']
    )
    try:
        db.session.add(c)
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return abort(400)
#Delete selected id from course Table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    c = Course.query.get_or_404(id, 'Course ID not found')
    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing course
@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    c = Course.query.get_or_404(id)
    if 'name' not in request.json and 'start_date' not in request.json and 'end_date' not in request.json:
        return abort(400)
    if 'name' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        else:   
            c.name = request.json['name']
    if 'start_date' in request.json:
        c.start_date = request.json['start_date']
    if 'end_date' in request.json:
        c.end_date = request.json['end_date']
    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)
    
#retreaving students enroll in course by id
@bp.route('/<int:id>/students', methods=['GET'])
def students(id: int):
    c = Course.query.get_or_404(id, "This course isn't registered.")
    result = []
    for i in c.students:
        result.append(i.serialize())
    if not result:
        return abort(400, "No students sign up for this course.")
    else:
        return jsonify(result)

#retreaving prfessor teach course
@bp.route('/<int:id>/pro_course', methods=['GET'])
def pro_course(id: int):
    c = Course.query.get_or_404(id, "Course not found")
    result = []
    for i in c.pro_course:
        result.append(i.serialize())
        result.append(c.serialize())
    if not result:
        return abort(400, "This course has no professor assigned")
    else:
        return jsonify(result)

