import json


def test_register(test_app_with_db):
    response = test_app_with_db.post(
        "/auth/register/",
        data=json.dumps(
            {
                "username": "test_user",
                "email": "huis.trevor@test.com",
                "full_name": "Trevor Huisintveld",
                "password": "test123",
            }
        ),
    )

    assert response.status_code == 201
    assert response.json()["username"] == "test_user"
    assert response.json()["email"] == "huis.trevor@test.com"
    assert response.json()["full_name"] == "Trevor Huisintveld"


def test_register_duplicate(test_app_with_db):
    response = test_app_with_db.post(
        "/auth/register/",
        data=json.dumps(
            {
                "username": "test_user",
                "email": "huis.trevor@test.com",
                "full_name": "Trevor Huisintveld",
                "password": "test123",
            }
        ),
    )

    assert response.status_code == 422


def test_login(test_app_with_db):
    response = test_app_with_db.post(
        "auth/login/",
        data={"username": "test_user", "password": "test123"},
    )

    assert response.status_code == 200
    assert response.json()["access_token"] is not None


def test_login_failure(test_app_with_db):
    response = test_app_with_db.post(
        "auth/login/",
        data={"username": "test_user", "password": "test1234"},
    )

    assert response.status_code == 401
