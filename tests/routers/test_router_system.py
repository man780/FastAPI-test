def test_health_check(test_app):
    response = test_app.get("/health/check")
    assert response.status_code == 200
    # assert response.json() == {"ping": "pong!"}
