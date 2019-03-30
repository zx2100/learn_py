import sys


def application(env, start_response):


    status = "200 ok"
    headers = [
        ("Server", "Test"),
        ("Content-Type", "text/html")
    ]

    start_response(status, headers)
    return sys.platform
