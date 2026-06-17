import requests

try:
    session = requests.Session()
    session.post('http://localhost:5000/login', data={'username': 'aj', 'password': 'password123'})
    resp = session.post('http://localhost:5000/api/solve', data={'expression': 'x^2 - 4 = 0'})
    print("Status code:", resp.status_code)
    print("Response text:", resp.text[:500])
except Exception as e:
    print("Error:", e)
