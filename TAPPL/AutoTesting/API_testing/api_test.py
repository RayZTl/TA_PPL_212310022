import requests

# API Endpoint
url = 'https://api.orangehrm.com/'

# Test Case: Verify API endpoint availability
def test_api_availability():
    response = requests.get(url)
    assert response.status_code == 200
    print("API is reachable.")

# Execute API test case
test_api_availability()
