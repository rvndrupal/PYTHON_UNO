import urllib

from urllib  import request

resp=request.urlopen("https://www.wikipedia.org")
print(resp)

print(resp.code)

print(resp.length)


data=resp.read()

len(data)

print(len(data))

html=data.decode("UTF-8")

print(html)