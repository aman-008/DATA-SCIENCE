import requests

r = requests.get('https://api.github.com/users/aman-008')
print(r.text)