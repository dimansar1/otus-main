from flask.testing import FlaskClient
from pytest import fixture
from .app import app

@fixture
def client() -> FlaskClient:
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

def test_check_the_page_index_status(client):
    url = "/"
    response = client.get(url)
    assert response.status_code == 200

def test_check_the_page_about_status(client):
    url = "/about/"
    response = client.get(url)
    assert response.status_code == 200
    