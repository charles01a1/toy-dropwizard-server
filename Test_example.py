import requests 
import json

def test_code() :
    r = requests. get('http://localhost:8085')
    json_response = r. json()
    assert json_response ["code"] == 404
    
def test_message():
    r = requests.get('http://localhost:8085')
    json_response = r.json()
    assert json_response["message"] == "HTTP 404 Not Found"
    
# def test_correct_code() :
#     r = requests. get('http://localhost:8085/hello-world')
#     json_response = r. json()
#     assert json_response ["id"] == 2
    
def test_correct_message():
    r = requests.get('http://localhost:8085/hello-world')
    json_response = r.json()
    assert json_response["content"] == "Hello, Stranger!"