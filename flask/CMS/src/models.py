import datetime

from flask_sqlalchemy import SQLAlchemy
#What you need into input when starting up
# pgAdmin server: http://localhost:5433/browser/
#. venv/scripts/activate
#cd flask/CMS
#flask run
db = SQLAlchemy()
#User Account table
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

    def __init__(self, name: str, useraccount_id: int):
           self.name = name,
           self.useraccount_id = useraccount_id
    
    def serialize(self):
           return {
                  'id': self.id,
                  'name': self.name,
                  'useraccount_id': self.useraccount_id
           }