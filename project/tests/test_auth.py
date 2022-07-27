import json


def test_register(test_app_with_db):
    response = test_app_with_db.post(
        "/auth/register/",
        data=json.dumps(
            {
                "username": "trevorhuis",
                "email": "huis.trevor@test.com",
                "full_name": "Trevor Huisintveld",
                "password": "test123",
            }
        ),
    )

    assert response.status_code == 201
    assert response.json()["username"] == "trevorhuis"
    assert response.json()["email"] == "huis.trevor@test.com"
    assert response.json()["full_name"] == "Trevor Huisintveld"


def test_login(test_app_with_db):
    response = test_app_with_db.post(
        "auth/login/",
        data={"username": "trevorhuis", "password": "test123"},
    )

    assert response.status_code == 200
    assert response.json()["access_token"] is not None
