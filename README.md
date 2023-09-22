#Course Management System
####SQL Portfolio Project 
#####by Spencer Klessens

This *CMS* is uesed for universities to store information 
as four categories; students, professors courses and useraccounts.
Each category has there own tables and they contains *unique* 
ID's and additional information. Below, each category with will
have a list of variables with there own requirments and rules.
(any veriable that has *unique* requirment can **not** be duplicated
in the table.)

**useraccounts**
    - username
        - must be 3 characters long
        - *unique*
        - is required.

    - password
        - must be 8 characters long
        - is required
        - does **not** have to be *unique*

    - email
        - **not** required
        - must be *unique*

    - user status
        - shows if user account is a student or professor.
        - is required.

**students**
    - name
        - name of the student enrolled,
        - is required.

    - useraccount_id
        - students useraccount id 
        - is required
        - must be from useraccounts table

    -course_id
        - student current course enrollment.
        - **not** required
        - if filled must be from courses table

**professors**
    - name
        - name of employied professor,
        - is required.

    - useraccount_id
        - professors useraccount id 
        - is required
        - must be from useraccounts table

**course**
    - name
        - name of the course
        - is required
    - start_date
        - date and time when course begins
        - year-month-day *yyyy-mm-dd*
        - hour-minuite-second *hh-mm-ss*
        - ir required
    - end_date
        - date and time when course begins
        - year-month-day *yyyy-mm-dd*
        - hour-minuite-second *hh-mm-ss*
        - is required

#####API
Below are referances for each table 
containg endpoints, methods and parameters.
They can be use with any open source desktop
application.

- **index**: loads all data from table
- **shows**: loads one data row from table base on ID 
- **create**: create new row for table
- **delete**: deletes selected row from table
- **update**: updates or patches selected row from table
- **students**: loads all students enroll in a single course
- **pro_course**: loads professor info and course there assign too
- **course_pro**: loads course info and professor thats assign too

**useraccounts**

|            endpoints            |  mehtods |  parameters   |
|---------------------------------|----------|---------------|
|http://servername/useraccounts   |   index  |     none      |
|http://servername/useraccounts/id|   shows  |  **integer**  |
|http://servername/useraccounts   |  create  |     none      |
|http://servername/useraccounts/id|  delete  |  **integer**  |
|http://servername/useraccounts/id|  update  |  **integer**  |

**students**

|            endpoints            |  mehtods |  parameters   |
|---------------------------------|----------|---------------|
|http://servername/students       |   index  |     none      |
|http://servername/students/id    |   shows  |  **integer**  |
|http://servername/students       |  create  |     none      |
|http://servername/students/id    |  delete  |  **integer**  |
|http://servername/students/id    |  update  |  **integer**  |

**courses**

|                endpoints                  |  mehtods |  parameters   |
|-------------------------------------------|----------|---------------|
|http://servername/courses                  |   index  |     none      |
|http://servername/courses/id               |   shows  |  **integer**  |
|http://servername/courses                  |  create  |     none      |
|http://servername/courses/id               |  delete  |  **integer**  |
|http://servername/courses/id               |  update  |  **integer**  |
|http://localhost:5000/courses/id/students  | students |  **integer**  |
|http://localhost:5000/courses/id/pro_course|pro_course|  **integer**  |

**professors**

|                   endpoints                  |  mehtods |  parameters   |
|----------------------------------------------|----------|---------------|
|http://servername/professors                  |   index  |     none      |
|http://servername/professors/id               |   shows  |  **integer**  |
|http://servername/professors                  |  create  |     none      |
|http://servername/professors/id               |  delete  |  **integer**  |
|http://servername/professors/id               |  update  |  **integer**  |
|http://localhost:5000/professors/id/course_pro|course_pro|  **integer**  |

1.) How did the project's design evolve over time?
    During my time working on my CMS, I came up ideas I could use for it and how it would work.

2.) Did you choose to use an ORM or raw SQL? Why?
    I use ORM.  I have a better understanding wiht ptyhon then with SQL so I went with that.

3.) What future improvements are in store, if any?
    If I do return to my CMS I would look back on my original Entiry-relationship diagram
    for ideas and find ways to improve on my current version.# SQlproject
# SQlproject
