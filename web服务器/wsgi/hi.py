
def application(env, start_response):
    status = "200 ok"
    headres = [
        ("Server", "Test"),
        ("Content-Type", "text/html")
    ]

    start_response(status, headres)

    return "Hi"

