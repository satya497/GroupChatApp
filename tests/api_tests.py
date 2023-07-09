import requests

# API base URL
base_url = 'http://localhost:5000'

# Test case: Create user
def test_create_user():
    # Endpoint URL
    url = f'{base_url}/admin/create_user'

    # Request payload
    payload = {
        "username": "Satya",
        "password": "Satya123",
        "user_details": {"user":"Satya","pwd":"Satya123"}
    }

    # Send POST request to create user
    response = requests.post(url, json=payload)

    # Verify response status code
    assert response.status_code == 200

    # Verify response message
    response_data = response.json()
    assert response_data['message'] == 'User created successfully'


# Test case: Login
def test_login():
    # Endpoint URL
    url = f'{base_url}/auth/login'

    # Request payload
    payload = {
        'username': 'test_user',
        'password': 'password123'
    }

    # Send POST request to login
    response = requests.post(url, json=payload)

    # Verify response status code
    assert response.status_code == 200

    # Verify response message
    response_data = response.json()
    assert response_data['message'] == 'Login successful'


# Test case: Create group
def test_create_group():
    # Endpoint URL
    url = f'{base_url}/groups/create_group'

    # Request payload
    payload = {
        'group_name': 'test_group'
    }

    # Send POST request to create group
    response = requests.post(url, json=payload)

    # Verify response status code
    assert response.status_code == 200

    # Verify response message
    response_data = response.json()
    assert response_data['message'] == 'Group created successfully'


# Run the tests
test_create_user()
test_login()
test_create_group()

print('All tests passed successfully.')
