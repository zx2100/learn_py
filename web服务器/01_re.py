import re


pattern = "/\w*\.?\w*"

s = "POST /indeasdx.htm sl HTTP/1.1"

a = re.search(pattern, s)

print(a.group()) 