from flask import Blueprint, jsonify, abort, request
from ..models import Student, User_Account, Course, Professor, cp_table, db

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    accounts = Student.query.all() # ORM performs SELECT query
    result = []
    for t in accounts:
        result.append(t.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

#retrieves selected student by id number
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    s = Student.query.get_or_404(id, "Student not found")
    return jsonify(s.serialize())

#creates a new student row
@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json or 'useraccount_id' not in request.json or 'course_id' not in request.json:
        return abort(400)
    elif len(request.json['name']) < 3:
        return abort(400)
    s = Student(
        name=request.json['name'],
        useraccount_id=request.json['useraccount_id'],
        course_id=request.json['course_id']
    )
    try:
        db.session.add(s)
        db.session.commit()
        return jsonify(s.serialize())
    except:
        return abort(400)
    
#Delete selected id from students Table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    s = Student.query.get_or_404(id, 'Professor ID not found')
    try:
        db.session.delete(s)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing students
@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    s = Student.query.get_or_404(id)
    if 'name' not in request.json and 'useraccount_id' not in request.json and 'course_id' not in request.json:
        return abort(400)
    if 'name' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        else:
            s.name = request.json['name']
    if 'useraccount_id' in request.json:
        s.useraccount_id = request.json['useraccount_id'] 
    if 'course_id' in request.json:
        s.course_id = request.json['course_id']
    try:
        db.session.commit()
        return jsonify(s.serialize())
    except:
        return jsonify(False)