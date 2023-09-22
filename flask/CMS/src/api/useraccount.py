from flask import Blueprint, jsonify, abort, request
from ..models import User_Account, Student, Professor, db
import hashlib, secrets, re
#to protect password
def scramble(password: str):
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

#var that check if email is vaild
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

bp = Blueprint('useraccounts', __name__, url_prefix='/useraccounts')

#retrieves all useraccount's from useraccounts table
@bp.route('', methods=['GET'])
def index():
    useraccount = User_Account.query.all() 
    result = []
    for a in useraccount:
        result.append(a.serialize()) 
    return jsonify(result) 

#retrieves selected user account by id number
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User_Account.query.get_or_404(id, "User Accounts not found")
    return jsonify(u.serialize())

#creates a new user account row
@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json or 'user_status' not in request.json:
        return abort(400)
    elif len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    elif request.json['user_status'] != 'student' and request.json['user_status'] != 'professor':
        return abort(400)
    elif request.json['email'] is not None:
        if re.fullmatch(regex, request.json['email']):
            print()
        else:
            return abort(400)
    u = User_Account (
        username=request.json['username'],
        password=scramble(request.json['password']),
        email=request.json['email'],
        user_status=request.json['user_status'],
    )
    #Prevent 500 error if unique name or email is uesed again
    #for b in User_Account.query.all():
        #if u.username == b.username or u.email == b.email:
            #return abort(400)
    try:
        db.session.add(u) # prepare CREATE useraccount
        db.session.commit()# execute CREATE useraccount
        return jsonify(u.serialize())
    except:
        return abort(400)

#Deletes slected id for useraccounts Table
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User_Account.query.get_or_404(id, "User Account not found")
    try:
        db.session.delete(u) # prepare DELETE useraccount
        db.session.commit() # execute DELETE useraccount
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing user account
@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    u = User_Account.query.get_or_404(id)
    if 'username' not in request.json and 'password' not in request.json and 'user_status' not in request.json and 'email' not in request.json:
        return abort(400)
    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        else:
            u.username = request.json['username']
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        else:
            u.password = scramble(request.json['password'])
    if 'email' in request.json:
        if re.fullmatch(regex, request.json['email']):
            u.email = request.json['email']
        else:
            u.email = User_Account.email
    if 'user_status' in request.json:
        if request.json['user_status'] != 'student' and request.json['user_status'] != 'professor':
            return abort(400)
        else:
            u.user_status = request.json['user_status']      
    try:
        db.session.commit() 
        return jsonify(u.serialize())
    except:
        return jsonify(False)