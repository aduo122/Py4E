import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

# while True:
    # address = input('Enter location: ')

url = "http://py4e-data.dr-chuck.net/comments_113417.xml"
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
# print(results)

res = 0

for r in results:
    res += int(r.find('count').text)

print(res)