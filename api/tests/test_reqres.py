import requests
import json
from jsonschema import validate
from pathlib import Path
from datetime import datetime


url = "https://reqres.in/api/users"


def schema_path(name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{name}'))


def test_get_single_user():
    response = requests.get(f'{url}/2')
    assert response.status_code == 200
    schema = schema_path("get_single_status_response.json")
    with open(schema) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_post_create():
    name = "Nikolay"
    job = "QA"
    today = datetime.utcnow().strftime("%Y-%m-%d")
    payload = {"name": name, "job": job}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    schema = schema_path("post_create_response.json")
    with open(schema) as file:
        validate(response.json(), schema=json.loads(file.read()))
    assert response.json()["name"] == name
    assert response.json()["job"] == job
    assert today in response.json()['createdAt']


def test_put_update():
    name = "Nikolay"
    job = "Team Lead QA"
    payload = {"name": name, "job": job}
    response = requests.put(f'{url}/2', data=payload)
    assert response.status_code == 200
    schema = schema_path("put_update_response.json")
    with open(schema) as file:
        validate(response.json(), schema=json.loads(file.read()))
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_delete():
    payload = {"name": "Nikolay", "job": "QA"}
    response = requests.delete(f'{url}/2', data=payload)
    assert response.status_code == 204
    assert response.text == ''


def test_get_not_found():
    payload = {"name": "Nikolay", "job": "Team Lead QA"}
    response = requests.get(f'{url}/unknown/2', data=payload)
    assert response.status_code == 404
    assert response.json() == {}


def test_post_login_unsuccessful():
    payload = {"email": "ntitenok@gmail.com"}
    response = requests.post('https://reqres.in/api/login', data=payload)
    assert response.status_code == 400
    schema = schema_path("post_login_unsuccessful_response.json")
    with open(schema) as file:
        validate(response.json(), schema=json.loads(file.read()))
    assert response.json() == {"error": "Missing password"}

def test_get_users_returns_unique_users():
    response = requests.get(
        url="https://reqres.in/api/users",
        params={"page": 2, "per_page": 4},
        verify=False
    )
    names = [element["first_name"] for element in response.json()["data"]]
    assert 'Tracey' and 'Michael' in names

