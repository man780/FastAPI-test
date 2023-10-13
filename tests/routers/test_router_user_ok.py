def test_user_create(test_app, random_user_data):
    response = test_app.post(
        "/user/create",
        json=random_user_data
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == random_user_data.get("username")
    assert response_data["email"] == random_user_data.get("email")
    assert response_data["full_name"] == random_user_data.get("full_name")


def test_user_get(test_app):
    user_id = 1
    response = test_app.get(f"/user/get/{user_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == "string"
    assert response_data["email"] == "string"
    assert response_data["full_name"] == "string"
    assert response_data["id"] == user_id


def test_user_update(test_app, random_user_data):
    user_id = 2
    response = test_app.put(
        f"/user/update/{user_id}",
        json=random_user_data
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == random_user_data.get("username")
    assert response_data["email"] == random_user_data.get("email")
    assert response_data["full_name"] == random_user_data.get("full_name")
    assert response_data["id"] == user_id


def test_user_delete(test_app):
    user_id = 3
    response = test_app.delete(
        f"/user/delete/{user_id}",
    )
    assert response.status_code == 404
