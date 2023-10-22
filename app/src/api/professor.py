from flask import Blueprint, jsonify, abort, request
from ..models import Course, Professor, cp_table, db

bp = Blueprint('professors', __name__, url_prefix='/professors')

#retrieves all professors id, name and useraccount id
@bp.route('', methods=['GET'])
def index():
    p = Professor.query.all() 
    result = []
    for i in p:
        result.append(i.serialize()) 
    return jsonify(result) 

#retrieves selected professor by id number
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Professor.query.get_or_404(id, "Professor not found")
    return jsonify(p.serialize())

#creates a new professor row
@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json or 'useraccount_id' not in request.json:
        return abort(400)
    elif len(request.json['name']) < 3:
        return abort(400)
    p = Professor(
        name=request.json['name'],
        useraccount_id=request.json['useraccount_id']
    )
    #Prevent 500 error if id in User_Account doens't exist
    try:
        db.session.add(p)
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return abort(400)

#Delete selected id from professors Table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Professor.query.get_or_404(id, 'Professor ID not found')
    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing professors
@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    p = Professor.query.get_or_404(id)
    if 'name' not in request.json and 'useraccount_id' not in request.json:
        return abort(400)
    if 'name' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        else:
            p.name = request.json['name']
    if 'useraccount_id' in request.json:
        p.useraccount_id = request.json['useraccount_id'] 
    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)
    
#Find professors course
@bp.route('/<int:id>/course_pro', methods=['GET'])
def course_pro(id: int):
    #c = Course.query.get_or_404(id, "Course not found")
    p = Professor.query.get_or_404(id, "Professor not found")
    #p = Professor.query.all()
    result = []
    for i in p.course_pro:
        result.append(i.serialize())
        result.append(p.serialize())
    if not result:
        return abort(400, 'Professor not assign to any course.')
    else:
        return jsonify(result)