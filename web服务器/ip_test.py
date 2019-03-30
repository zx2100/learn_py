import os

def get_ip():
    status = "200 ok"

    headers = [
        ("Server", "Myserver"),
        ("Content-Type", "text/html; chatset=utf-8")
    ]
    #start_response(status, headers)
    # 返回IP信息
    result = os.popen("ifconfig").read()

    return result.encode("utf-8")



print (bytes(get_ip()))

