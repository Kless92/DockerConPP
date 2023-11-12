<h1>Course Management System</h1>

<h3>SQL Portfolio Project</h3>

<h4>by Spencer Klessens</h4>

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
        - is required
        - must be *unique*

    - user_status
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

    - grad_student
        - bool "true" or "false"
        - is required

    - sub
        - bool "true" or "false"
        - is required

**courses**

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
    - room
        - course buildings id
        - not required

**buildings**

    -name
        - name of the building
        - is required
    -room
        -room name in the building
        -is required
    -course_id
        - buildings course id
        -is required

<h4>API</h4>

Below are referances for each table 
containg endpoints, methods and parameters.
They can be use with any open source desktop
application. (Its recommended to use SQLAlchemy flask. 
If you are make sure to type "flask run" in the command promt.)

- **index**: loads all data from table
- **shows**: loads one data row from table base on ID 
- **create**: create new row for table
- **delete**: deletes selected row from table
- **update**: updates or patches selected row from table
- **students**: loads all students enroll in a single course
- **pro_course**: loads professor info and course there assign too
- **course_pro**: loads course info and professor thats assign too

**useraccounts**

|                endpoints                   |  mehtods |  parameters   |
|---------------------------------|----------|----------|               |
|http://servername:port/useraccounts         |   index  |     none      |
|http://servername:port/useraccounts/id      |   shows  |  **integer**  |
|http://servername:port/useraccounts         |  create  |     none      |
|http://servername:port/useraccounts/id      |  delete  |  **integer**  |
|http://servername:port/useraccounts/id      |  update  |  **integer**  |

**students**

|               endpoints              |  mehtods |  parameters   |
|--------------------------------------|----------|---------------|
|http://servername:port/students       |   index  |     none      |
|http://servername:port/students/id    |   shows  |  **integer**  |
|http://servername:port/students       |  create  |     none      |
|http://servername:port/students/id    |  delete  |  **integer**  |
|http://servername:port/students/id    |  update  |  **integer**  |

**courses**

|                   endpoints                    |  mehtods |  parameters   |
|------------------------------------------------|----------|---------------|
|http://servername:port/courses                  |   index  |     none      |
|http://servername:port/courses/id               |   shows  |  **integer**  |
|http://servername:port/courses                  |  create  |     none      |
|http://servername:port/courses/id               |  delete  |  **integer**  |
|http://servername:port/courses/id               |  update  |  **integer**  |
|http://servername:port/courses/id/students      | students |  **integer**  |
|http://servername:port/courses/id/pro_course    |pro_course|  **integer**  |
|http://servername:port/courses/id/room          |  room    |  **integer**  |

**professors**

|                      endpoints                    |  mehtods  |  parameters   |
|---------------------------------------------------|-----------|---------------|
|http://servername:port/professors                  |   index   |     none      |
|http://servername:port/professors/id               |   shows   |  **integer**  |
|http://servername:port/professors                  |  create   |     none      |
|http://servername:port/professors/id               |  delete   |  **integer**  |
|http://servername:port/professors/id               |  update   |  **integer**  |
|http://servername:port/professors/id/course_pro    |course_pro |  **integer**  |
|http://servername:port/professors/gradStudent      |gradStudent|     none      |
|http://servername:port/professors/subsititues      |subsititues|     none      |

**buildings**

|                      endpoints                    |  mehtods  |  parameters   |
|---------------------------------------------------|-----------|---------------|
|http://servername:port/buildings                   |   index   |     none      |
|http://servername:port/buildings/id                |   shows   |  **integer**  |
|http://servername:port/buildings                   |  create   |     none      |
|http://servername:port/buildings/id                |  delete   |  **integer**  |
|http://servername:port/buildings/id                |  update   |  **integer**  |
|http://servername:port/courses/id/change           |   change  |  **interger** |
