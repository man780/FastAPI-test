def test_user_create(test_app):
    new_user = {
        "username": "Some5",
        "email": "some5@email.ss",
        "full_name": "string5 tets"
    }
    response = test_app.post(
        "/user/create",
        json=new_user
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == new_user.get("username")
    assert response_data["email"] == new_user.get("email")
    assert response_data["full_name"] == new_user.get("full_name")


def test_user_get(test_app):
    response = test_app.get("/user/get/1")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == "string"
    assert response_data["email"] == "string"
    assert response_data["full_name"] == "string"
    assert response_data["id"] == 1
