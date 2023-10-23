from flask import url_for
import pytest, requests
#import app #import indexUA
#https://www.lambdatest.com/learning-hub/pytest-api-testing fro ref

#GetUA, GetStu, GetPro and GetCour check if the url is live.
def test_GetUA():
    url = "http://localhost:5000/useraccounts"
    response = requests.get(url)
    assert response.status_code == 200
def test_GetStu():
    url = "http://localhost:5000/students"
    response = requests.get(url)
    assert response.status_code == 200
def test_GetPro():
    url = "http://localhost:5000/professors"
    response = requests.get(url)
    assert response.status_code == 200
def test_GetCour():
    url = "http://localhost:5000/courses"
    response = requests.get(url)
    assert response.status_code == 200

"""     url = "https://localhost:5000/useraccounts"
    data = {
        "username":
    }
    response = requests.get(url, data=data)
    assert response.status_code == 201 """