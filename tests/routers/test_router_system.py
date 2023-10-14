def test_health_check(test_app):
    response = test_app.get("/health/check")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Success"
    assert response_data["status"] is True


def test_health_check_db(test_app):
    response = test_app.get("/health/check/db")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "DB connection is: OK"
    assert response_data["status"] is True
