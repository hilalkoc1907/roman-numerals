from app import app


def test_api_gecerli():
    client = app.test_client()
    r = client.get("/api/convert?roman=MCMXCIV")
    assert r.status_code == 200
    assert r.get_json() == {"roman": "MCMXCIV", "value": 1994}


def test_api_kucuk_harf():
    client = app.test_client()
    r = client.get("/api/convert?roman=iv")
    assert r.get_json()["value"] == 4


def test_api_gecersiz():
    client = app.test_client()
    r = client.get("/api/convert?roman=IIII")
    assert r.status_code == 400
    assert "error" in r.get_json()


def test_api_sayidan_romaya():
    client = app.test_client()
    r = client.get("/api/to_roman?number=1994")
    assert r.status_code == 200
    assert r.get_json() == {"number": 1994, "roman": "MCMXCIV"}


def test_api_sayidan_romaya_gecersiz():
    client = app.test_client()
    for bad in ["0", "5000", "abc", "", "3.5"]:
        r = client.get("/api/to_roman?number=" + bad)
        assert r.status_code == 400
        assert "error" in r.get_json()