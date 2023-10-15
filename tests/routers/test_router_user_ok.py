"""
test router user for OK scenarios
"""


def test_user_create(test_app, random_user_data):
    """
    test user create router
    :param test_app:
    :param random_user_data:
    :return:
    """
    response = test_app.post("/user/create", json=random_user_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == random_user_data.get("username")
    assert response_data["email"] == random_user_data.get("email")
    assert response_data["full_name"] == random_user_data.get("full_name")


def test_user_get(test_app):
    """
    test user get router
    :param test_app:
    :return:
    """
    user_id = 1
    response = test_app.get(f"/user/get/{user_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == "string"
    assert response_data["email"] == "string"
    assert response_data["full_name"] == "string"
    assert response_data["id"] == user_id


def test_user_update(test_app, random_user_data):
    """
    test user update router
    :param test_app:
    :param random_user_data:
    :return:
    """
    user_id = 2
    response = test_app.put(f"/user/update/{user_id}", json=random_user_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == random_user_data.get("username")
    assert response_data["email"] == random_user_data.get("email")
    assert response_data["full_name"] == random_user_data.get("full_name")
    assert response_data["id"] == user_id


def test_user_delete(test_app):
    """
    test user delete
    :param test_app:
    :return:
    """
    user_id = 3
    response = test_app.delete(
        f"/user/delete/{user_id}",
    )
    assert response.status_code == 404


def test_users_list(test_app):
    """
    test user list each (Check for each item is DICT)
    :param test_app:
    :return:
    """
    response = test_app.get("/user/list")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) > 0
    for user in response_data:
        assert isinstance(user, type({}))


def test_users_list_items(test_app):
    """
    test users list items type (Check for each item has keys)
    :param test_app:
    :return:
    """
    response = test_app.get("/user/list")
    response_data = response.json()
    assert len(response_data) > 0
    for user in response_data:
        assert isinstance(user.get("username"), type(str()))
        assert isinstance(user.get("email"), type(str()))
