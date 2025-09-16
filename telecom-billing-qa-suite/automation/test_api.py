import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

# Test GET /users
response = requests.get(f'{BASE_URL}/users')
assert response.status_code == 200
print('GET /users test passed')

# Test GET /posts/1
response = requests.get(f'{BASE_URL}/posts/1')
assert response.status_code == 200
print('GET /posts/1 test passed')
