import sys
import dynamic_server
import os

class Application(object):
    """路由请求URI"""
    def __call__(self, env, start_response):

        query_url = env.get("PATH_INFO", "/")
        # print(query_url)
        for url, app in urls:
            if query_url == url:
                result = app(env, start_response)
                # print(result)
                return result
        return None


def get_ip(env, start_response):
    status = "200 ok"

    headers = [
        ("Server", "Myserver"),
        ("Content-Type", "text/plain; charset=UTF-8")
    ]
    start_response(status, headers)
    # 返回IP信息
    result = os.popen("ifconfig").read()

    return result.encode("utf-8")


def get_version(env, start_response):
    status = "200 ok"

    headers = [
        ("Server", "Myserver"),
        ("Content-Type", "text/html")
    ]
    start_response(status, headers)
    # 返回系统信息
    return sys.platform.encode("utf-8")

def get_ss_status(env, start_response):
    status = "200 ok"

    headers = [
        ("Server", "Myserver"),
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    # 返回套接字信息
    result = os.popen("ss -tanp").read()
    return result.encode("utf-8")

# 请求路由
urls = [
    ("/ip", get_ip),
    ("/version", get_version),
    ("/ss", get_ss_status)
]



app = Application()


http_server = dynamic_server.Httpserver(app)

http_server.start()
