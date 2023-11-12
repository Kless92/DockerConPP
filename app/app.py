import datetime
from flask import Flask, Blueprint, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
import hashlib, secrets, re

app = Flask(__name__, )
db = SQLAlchemy()

app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin123@cms.c0h1kjfybabt.us-east-2.rds.amazonaws.com/cms_db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )
db.init_app(app)

class User_Account(db.Model):
    __tablename__='useraccounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True)
    user_status = db.Column(db.String(128), nullable=False)

    def __init__(self, username: str, password: str, email: str, user_status: str):
                 self.username = username
                 self.password = password
                 self.email = email
                 self.user_status = user_status

    def serialize(self):
          return {
                'id': self.id,
                'username': self.username,
                'password': self.password,
                'email': self.email,
                'user_status': self.user_status
          }
#Student table
class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    useraccount_id = db.Column(db.Integer, db.ForeignKey('useraccounts.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    #course = db.relationship('Course', backref='students', lazy=True)

    def __init__(self, name: str, useraccount_id: int, course_id: int):
                 self.name = name
                 self.useraccount_id = useraccount_id
                 self.course_id = course_id

    def serialize(self):
          return {
                'id': self.id,
                'name': self.name,
                'useraccount_id': self.useraccount_id,
                'course_id': self.course_id
          }
#course professor table
cp_table = db.Table('courses_professors',
                     db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True),
                     db.Column('professor_id', db.Integer, db.ForeignKey('professors.id'), primary_key=True))
#Course table
class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    end_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    students = db.relationship('Student', backref='course', lazy=True)
    pro_course = db.relationship('Professor', secondary=cp_table, lazy='subquery',
                                  backref=db.backref('course_pro',lazy=True))
    roNum = db.relationship('Building', backref='course', lazy=True)    
    
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
           self.name = name,
           self.start_date = start_date,
           self.end_date = end_date

    def serialize(self):
           return {
                  'id': self.id,
                  'name': self.name,
                  'start_date': self.start_date.isoformat(),
                  'end_date': self.end_date.isoformat()
           }
#Professor table
class Professor(db.Model):
    __tablename__='professors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    useraccount_id = db.Column(db.Integer, db.ForeignKey('useraccounts.id'), nullable=False)
    grad_student = db.Column(db.Boolean, nullable=False)
    sub = db.Column(db.Boolean, nullable=False)

    def __init__(self, name: str, useraccount_id: int, grad_student: bool, sub: bool):
            self.name = name,
            self.useraccount_id = useraccount_id
            self.grad_student = grad_student
            self.sub = sub
    def serialize(self):
           return {
                  'id': self.id,
                  'name': self.name,
                  'useraccount_id': self.useraccount_id,
                  'grad_student': self.grad_student,
                  'sub': self.sub
           }

#Building table
class Building(db.Model):
    __tablename__='buildings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    room = db.Column(db.String(128), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, name: str, room: str, course_id: int):
        self.name = name,
        self.room = room,
        self.course_id = course_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'room': self.room,
            'course_id': self.course_id
        }
#to protect password
def scramble(password: str):
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

#var that check if email is vaild
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

###################################
#########User Accounts API#########
###################################
#retrieves all useraccount's from useraccounts table
@app.route('/useraccounts', methods=['GET'])
def indexUA():
    useraccount = User_Account.query.all() 
    result = []
    for a in useraccount:
        result.append(a.serialize()) 
    return jsonify(result) 

#retrieves selected user account by id number
@app.route('/useraccounts/<int:id>', methods=['GET'])
def showUA(id: int):
    u = User_Account.query.get_or_404(id, "User Accounts not found")
    return jsonify(u.serialize())

#creates a new user account row
@app.route('/useraccounts', methods=['POST'])
def createUA():
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
@app.route('/useraccounts/<int:id>', methods=['DELETE'])
def deleteUA(id: int):
    u = User_Account.query.get_or_404(id, "User Account not found")
    try:
        db.session.delete(u) # prepare DELETE useraccount
        db.session.commit() # execute DELETE useraccount
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing user account
@app.route('/useraccounts/<int:id>', methods=['PATCH','PUT'])
def updateUA(id: int):
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

###################################
###########Students API############
###################################
#retrieves all student's info from studnets table
@app.route('/students', methods=['GET']) 
def indexStu():
    accounts = Student.query.all() 
    result = []
    for t in accounts:
        result.append(t.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

#retrieves selected student by id number
@app.route('/students/<int:id>', methods=['GET'])
def showStu(id: int):
    s = Student.query.get_or_404(id, "Student not found")
    return jsonify(s.serialize())

#creates a new student row
@app.route('/students', methods=['POST'])
def createStu():
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
@app.route('/students/<int:id>', methods=['DELETE'])
def deleteStu(id: int):
    s = Student.query.get_or_404(id, 'Professor ID not found')
    try:
        db.session.delete(s)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing students
@app.route('/students/<int:id>', methods=['PATCH','PUT'])
def updateStu(id: int):
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
###################################
##########Professors API###########
###################################
#retrieves all professors's info from professors table
@app.route('/professors', methods=['GET'])
def proindex():
    p = Professor.query.all() 
    result = []
    for i in p:
        result.append(i.serialize()) 
    return jsonify(result) 

#retrieves selected professor by id number
@app.route('/professors/<int:id>', methods=['GET'])
def proshow(id: int):
    p = Professor.query.get_or_404(id, "Professor not found")
    return jsonify(p.serialize())

#creates a new professor row
@app.route('/professors', methods=['POST'])
def procreate():
    if 'name' not in request.json or 'useraccount_id' not in request.json and 'grad_student' not in request.json and 'sub' not in request.json:
        return abort(400)
    elif len(request.json['name']) < 3:
        return abort(400)
    elif request.json['grad_student'] != True and request.json['grad_student'] != False:
        return abort(400)
    elif request.json['grad_student'] != True and request.json['grad_student'] != False:
        return abort(400)
    p = Professor(
        name=request.json['name'],
        useraccount_id=request.json['useraccount_id'],
        grad_student=request.json['grad_student'],
        sub=request.json['sub']
    )
    #Prevent 500 error if id in User_Account doens't exist
    try:
        db.session.add(p)
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return abort(400)

#Delete selected id from professors Table
@app.route('/professors/<int:id>', methods=['DELETE'])
def prodelete(id: int):
    p = Professor.query.get_or_404(id, 'Professor ID not found')
    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing professors
@app.route('/professors/<int:id>', methods=['PATCH','PUT'])
def proupdate(id: int):
    p = Professor.query.get_or_404(id)
    if 'name' not in request.json and 'useraccount_id' not in request.json and 'grad_student' not in request.json and 'sub' not in request.json:
        return abort(400)
    if 'name' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        else:
            p.name = request.json['name']
    if 'useraccount_id' in request.json:
        p.useraccount_id = request.json['useraccount_id'] 
    if 'grad_student' in request.json:
        if request.json['grad_student'] != True and request.json['grad_student'] != False:
            return abort(400)
        else:
            p.useraccount_id = request.json['grad_student'] 
    if 'sub' in request.json:
        if request.json['grad_student'] != True and request.json['grad_student'] != False:
            return abort(400)
        else:
            p.useraccount_id = request.json['grad_student'] 
    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)
    
#Find professors course
@app.route('/professors/<int:id>/course_pro', methods=['GET'])
def procourse_pro(id: int):
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
    
#Show all professors that are grad students
@app.route('/professors/gradStudent', methods=['GET'])
def prograd():
    p = Professor.query.all() 
    result = []
    for i in p:
        if i.grad_student == True:
            result.append(i.serialize()) 
    if not result:
        return abort(400, 'No grad students were found.')
    return jsonify(result) 

#Show all professors that can be substitutes
@app.route('/professors/substitutes', methods=['GET'])
def prosub():
    p = Professor.query.all() 
    result = []
    for i in p:
        if i.sub == True:
            result.append(i.serialize()) 
    if not result:
        return abort(400, 'No available substitutes were found.')
    return jsonify(result) 

###################################
############Course API#############
###################################
#retrieves all course's from courses table
@app.route('/courses', methods=['GET']) # decorator takes path and list of HTTP verbs
def corindex():
    c = Course.query.all() # ORM performs SELECT query
    result = []
    for i in c:
        result.append(i.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

#retrieves selected course by id number
@app.route('/courses/<int:id>', methods=['GET'])
def corshow(id: int):
    c = Course.query.get_or_404(id, "Course not found")
    return jsonify(c.serialize())

#creates a new course row
@app.route('/courses', methods=['POST'])
def corcreate():
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
@app.route('/courses/<int:id>', methods=['DELETE'])
def cordelete(id: int):
    c = Course.query.get_or_404(id, 'Course ID not found')
    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing course
@app.route('/courses/<int:id>', methods=['PATCH','PUT'])
def corupdate(id: int):
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
@app.route('/courses/<int:id>/students', methods=['GET'])
def corstudents(id: int):
    c = Course.query.get_or_404(id, "This course isn't registered.")
    result = []
    for i in c.students:
        result.append(i.serialize())
    if not result:
        return abort(400, "No students sign up for this course.")
    else:
        return jsonify(result)

#retreaving prfessor teach course
@app.route('/courses/<int:id>/pro_course', methods=['GET'])
def corpro_course(id: int):
    c = Course.query.get_or_404(id, "Course not found")
    result = []
    for i in c.pro_course:
        result.append(i.serialize())
        result.append(c.serialize())
    if not result:
        return abort(400, "This course has no professor assigned")
    else:
        return jsonify(result)

#Shows the building and room for course
@app.route('/courses/<int:id>/room', methods=['GET'])
def roomcourse(id: int):
    c = Course.query.get_or_404(id, "Course not found")
    result = []
    for i in c.roNum:
        result.append(i.serialize())
        result.append(c.serialize())
    if not result:
        return abort(400, "This course has no room assinged.")
    else:
        return jsonify(result)

###################################
###########Buildings API###########
###################################
#retrieves all building's info from buildings table
@app.route('/buildings', methods=['GET']) 
def indexBul():
    b = Building.query.all() 
    result = []
    for i in b:
        result.append(i.serialize()) 
    return jsonify(result) 

#retrieves selected bulding by id number
@app.route('/buildings/<int:id>', methods=['GET'])
def showBul(id: int):
    b = Building.query.get_or_404(id, "Building not found")
    return jsonify(b.serialize())

#creates a new building row
@app.route('/buildings', methods=['POST'])
def createBul():
    if 'name' not in request.json or 'room' not in request.json:
        return abort(400)
    elif len(request.json['name']) < 3:
        return abort(400)
    elif len(request.json['room']) < 3:
        return abort(400)
    b = Building(
        name=request.json['name'],
        room=request.json['room']
    )
    try:
        db.session.add(b)
        db.session.commit()
        return jsonify(b.serialize())
    except:
        return abort(400)
    
#Delete selected id from building Table
@app.route('/buildings/<int:id>', methods=['DELETE'])
def deleteBul(id: int):
    b = Building.query.get_or_404(id, 'Building ID not found')
    try:
        db.session.delete(b)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    
#Put/Patch existing building
@app.route('/buildings/<int:id>', methods=['PATCH','PUT'])
def updateBul(id: int):
    b = Building.query.get_or_404(id)
    if 'name' not in request.json and 'room' not in request.json:
        return abort(400)
    if 'course_id' in request.json:
        return abort(400)
    if 'name' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        else:   
            b.name = request.json['name']
    if 'room' in request.json:
        if len(request.json['room']) < 3:
            return abort(400)
        else:   
            b.room = request.json['room']
    try:
        db.session.commit()
        return jsonify(b.serialize())
    except:
        return jsonify(False)

#Changes the course_id of the selected building
@app.route('/courses/<int:id>/change', methods=['PATCH','PUT'])
def chBulcourse(id: int):
    b = Building.query.get_or_404(id)
    if 'name' in request.json and 'room' in request.json:
        return abort(400)
    if 'course_id' not in request.json:
        return abort(400)
    else:   
        b.course_id = request.json['course_id']
    try:
        db.session.commit()
        return jsonify(b.serialize())
    except:
        return jsonify(False)
    
###################################
########Basic Web Address##########
###################################
@app.route('/')
def main():
    return '<h1>Spencer K. CMS</h1><h2>There are Five Paths each with APIs.</h2><h2>* useraccounts<h2>*  students</h2><h2>* professors</h2><h2>* courses</h2><h2>* buildings</h2><h2>Type "pathname"/info for api path names.</h2><h2>It is recommended this is used with Insomnia.  Make sure the addresses are correct or a error will occur.</h2>'
@app.route('/useraccounts/info')
def infoUA():
    return '<h1>/useraccounts  GET</h1><h2>* retrieve all information on useraccounts.</h2><h1>/useraccount/id GET</h1><h2>* retrieves useraccount information base on selected id</h2><h1>/useraccount  POST</h1><h2>*  Create new useraccount if the requirment are meet.</h2><h1>/useraccount  DELETE</h1><h2>*  Delete a existing useraccount, if one exist.</h2><h1>/useraccounts/id PUT</h1><h2>* Edit slected useraccount if it exist.</h2>'
@app.route('/students/info')
def infoStu():
    return '<h1>/students  GET</h1><h2>* retrieve all information on students.</h2><h1>/useraccount/id GET</h1><h2>* retrieves student information base on selected id</h2><h1>/students  POST</h1><h2>*  Creates a new student row, if the requirment are meet.</h2><h1>/students  DELETE</h1><h2>*  Delete a existing students info, if one exist.</h2><h1>/students/id PUT</h1><h2>* Edit slected student info if it exist.</h2>'
@app.route('/professors/info')
def infoPro():
    return '<h1>/professors  GET</h1><h2>* retrieve all information on professors.</h2><h1>/professors/id GET</h1><h2>* retrieves professor information base on selected id</h2><h1>/professors  POST</h1><h2>*  Create new professor row, if the requirment are meet.</h2><h1>/professors  DELETE</h1><h2>*  Delete a existing professor, if one exist.</h2><h1>/useraccounts/id PUT</h1><h2>* Edit slected professor if it exist.</h2><h1>/professors/id/course_pro GET</h1><h2>* Retrieves the course that the professor will teach, if they are</h2><h1>/professors/gradStudent  GET</h1><h2>* Retrieves all professors that are also grad students, if there are any</h2><h1>/professors/substitutes  GET</h1><h2>*  Retrieves all professors that are available for substituting, if there are any'
@app.route('/courses/info')
def infoCou():
    return '<h1>/courses  GET</h1><h2>* retrieve all information on courses.</h2><h1>/courses/id GET</h1><h2>* retrieves course information base on selected id</h2><h1>/courses  POST</h1><h2>*  Create new course row if the requirment are meet.</h2><h1>/courses  DELETE</h1><h2>*  Delete a existing course, if one exist.</h2><h1>/courses/id PUT</h1><h2>* Edit slected course if it exist.</h2><h1>/courses/id/students  GET</h1><h2>* Retrieves all students info that are signup for selected course, if there are any</h2><h1>/courses/id/pro_course  GET</h1><h2>Retrieves professor that will teach selected course, if one is assigned</h2><h1>/courses/id/room  GET</h1><h2>* Retrieves building info that the course will be in, if one is assigned</h2>'
@app.route('/buildings/info')
def infoBul():
    return '<h1>/buildings  GET</h1><h2>* retrieve all information on buildings.</h2><h1>/buildings/id GET</h1><h2>* retrieves building information base on selected id</h2><h1>/buildings  POST</h1><h2>*  Create new building infomation if the requirment are meet.</h2><h1>/buildings  DELETE</h1><h2>*  Delete a existing building information, if one exist.</h2><h1>/buildings/id PUT</h1><h2>* Edit slected building, if it exist.</h2><h1>/courses/id/change  PUT</h1><h2>* Change what course would be tought in, if it vaild and not already assigned</h2>'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
