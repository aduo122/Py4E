import json
import urllib.request

url = "http://py4e-data.dr-chuck.net/comments_113418.json"
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)['comments']
print(info)
print('User count:', len(info))
res = 0
for item in info:
    res += int(item['count'])

print(res)