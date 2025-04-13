import requests

r = requests.get('https://api.github.com/users/aman-008')

# print(r.text)
with open("aman-008.txt", "w") as f:
    f.write(r.text)