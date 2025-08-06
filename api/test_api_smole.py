import requests

def test_signup_api():
    url = "https://my.functionhealth.com/signup?code=928AA4E1CD199B9D73A1A3B7DBC7F4F7"
    response = requests.get(url)
    assert response.status_code == 200
