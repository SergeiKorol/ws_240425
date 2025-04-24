import requests

def test_add():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 202
    assert response_body['completed'] == False

def test_completed():
    body = {"title": "test complete", "completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    task = response.json()

    assert task['completed'] == True

def test_add_123():
    body = {"title":"generated","completed":True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()['completed']

    assert response_body == True