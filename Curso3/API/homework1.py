import urllib.request
import json

url = input('Enter location: ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url = 'http://py4e-data.dr-chuck.net/comments_1938128.json'

if len(url) < 1:
    exit()
else:
    print('Retrieving', url)
    print('Retrieved', len(url), 'characters')
    
data = urllib.request.urlopen(url).read().decode()

json_data = json.loads(data)
# print(json_data)

sum = 0
for comment in json_data['comments']:
    sum += int(comment['count'])
    
print(sum)