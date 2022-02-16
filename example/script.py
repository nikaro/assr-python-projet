#!/usr/bin/python3

# https://docs.python-requests.org/en/latest/
import requests


def request_example(url):
    r = requests.get(url)
    return r.json()


def check_if_pwned_example(api_url, passwd):
    count = 0
    # your code here
    return count


def main():
    # your code here
    count = check_if_pwned_example( "https://my_url/api", "my_hash" )
    print(count)
    data = request_example("https://jsonplaceholder.typicode.com/todos/")
    # your code also here


if __name__ == "__main__":
    main()
