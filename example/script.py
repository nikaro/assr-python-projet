#!/usr/bin/python3

import requests


def request_example(url):
    # https://docs.python-requests.org/en/latest/
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    print(r.status_code)


def check_if_pwned_example(api_url, passwd):
    count = 0
    # your code here
    return count


def main():
    # your code here
    count = check_if_pwned_example("https://my_url/api", "my_hash")
    print(count)
    # your code also here
        


if __name__ == "__main__":
    main()
