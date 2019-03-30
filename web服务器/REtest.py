import re

test = '''GET /sdsad/sad HTTP/1.1
Host: 192.168.30.21
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://192.168.30.21/index.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
'''

#print(test)

pa1 = re.compile(r"^\s?[A-Z]*\s")
pa2 = re.compile(r"^\s?.* ")

method = pa1.search(test)
first_line =  pa2.search(test)
requery_path = re.search("/.*\s", first_line.group()).group().rstrip()

print(requery_path)
# root_path = "."
# file = open(root_path+requery_path)
# data = file.read()
# print(data)