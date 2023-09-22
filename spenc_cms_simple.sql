CREATE TABLE useraccounts(
    id SERIAL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE students(
    id SERIAL,
    name TEXT NOT NULL,
    useraccount_id INT NOT NULL,
    course_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE courses(
    id SERIAL,
    name TEXT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE professors(
    id SERIAL,
    name TEXT NOT NULL,
    useraccount_id INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE courses_professors(
    course_id INT NOT NULL,
    professor_id INT NOT NULL,
    PRIMARY KEY(course_id, professor_id)
);

ALTER TABLE students
ADD CONSTRAINT fk_students_useraccounts
FOREIGN KEY (useraccount_id)
REFERENCES useraccounts (id);

ALTER TABLE students
ADD CONSTRAINT fk_students_courses
FOREIGN KEY (course_id)
REFERENCES courses (id);

ALTER TABLE courses_professors
ADD CONSTRAINT fk_course_professors_courses
FOREIGN KEY (course_id)
REFERENCES courses (id);

ALTER TABLE courses_professors
ADD CONSTRAINT fk_course_professors_professors
FOREIGN KEY (professor_id)
REFERENCES professors (id);

ALTER TABLE professors
ADD CONSTRAINT fk_professors_useraccounts
FOREIGN KEY (useraccount_id)
REFERENCES useraccounts (id);

---ALTER TABLE that i might put in later
---If I need 2 student and profssors fk
---In useraccount table
ALTER TABLE useraccounts
ADD CONSTRAINT fk_students_id
FOREIGN KEY (student_id)
References students (id);

ALTER TABLE useraccounts
ADD CONSTRAINT fk_professors_id
FOREIGN KEY (professor_id)
References professors (id);