import xml.etree.ElementTree as ET
import urllib.request

url = input('Enter location: ')
print('Retrieving', url)
url_class = urllib.request.urlopen(url)
str = url_class.read()
xml = ET.fromstring(str)
xml_list = xml.findall('comments/comment')
print('Retrieved', len(str), 'characters')
print('Count:', len(xml_list))
sum = 0
for item in xml_list:
  sum += int(item.find('count').text)
  
print(f'Sum: {sum}')