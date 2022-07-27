import json


def test_create_budget(test_app_with_db):
    response = test_app_with_db.post(
        "/budgets/",
        data=json.dumps(
            {
                "month": 1,
                "year": 2020,
                "user_id": 1,
            }
        ),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {test_app_with_db.auth_token}",
        },
    )

    assert response.status_code == 201
    assert response.json()["month"] == 1
    assert response.json()["year"] == 2020
    assert response.json()["user_id"] == 1


def test_create_budgets_invalid_json(test_app_with_db):
    response = test_app_with_db.post(
        "/budgets/",
        data=json.dumps(
            {
                "month": 1,
                "year": 2020,
            }
        ),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {test_app_with_db.auth_token}",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "user_id"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_budget(test_app_with_db):
    response = test_app_with_db.post(
        "/budgets/",
        data=json.dumps(
            {
                "month": 1,
                "year": 2020,
                "user_id": 1,
            }
        ),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {test_app_with_db.auth_token}",
        },
    )
    budget_id = response.json()["id"]

    response = test_app_with_db.get(
        f"/budgets/{budget_id}",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {test_app_with_db.auth_token}",
        },
    )
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == budget_id
    assert response_dict["month"] == 1
    assert response_dict["year"] == 2020
    assert response_dict["user_id"] == 1


def test_read_budget_incorrect_id(test_app_with_db):
    response = test_app_with_db.get(
        "/budgets/999/",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {test_app_with_db.auth_token}",
        },
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "budget not found"
