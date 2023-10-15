"""
Tests for fail cases
"""


def test_user_create_with_type_error(test_app, random_user_data):
    """
    Test /user/create with type error
    :param test_app:
    :param random_user_data:
    :return:
    """
    random_user_data["username"] = True
    response = test_app.post("/user/create", json=random_user_data)
    assert response.status_code == 422
    response_data = response.json()
    assert len(response_data.get("detail")) > 0


def test_user_get_not_found(test_app):
    """
    Test /user/get/{user_id} with not existing user_id
    :param test_app:
    :return:
    """
    user_id = 100000
    response = test_app.get(f"/user/get/{user_id}")
    assert response.status_code == 404
    response_data = response.json()
    assert response_data["detail"] == "User not found"


#
def test_user_update_with_type_error(test_app, random_user_data):
    """
    Test /user/update/{user_id} with wrong type error
    :param test_app:
    :param random_user_data:
    :return:
    """
    user_id = 2
    random_user_data["username"] = True
    response = test_app.put(f"/user/update/{user_id}", json=random_user_data)
    assert response.status_code == 422
    response_data = response.json()
    assert len(response_data.get("detail")) > 0
