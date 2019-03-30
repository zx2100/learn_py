import time


def application(env, start_response):
    """返回现在时间，接受2个参数，env,start_response"""
    status = "200 ok"
    headers = [
        ("Server", "Test"),
        ("Content-Type", "text/html")
    ]

    start_response(status, headers)

    return  time.asctime()
