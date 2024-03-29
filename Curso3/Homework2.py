from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
  # Look at the parts of a tag
  # print('TAG:', tag)
  # print('URL:', tag.get('href', None))
  sum += int(tag.contents[0])
  # print('Contents:', tag.contents[0])
  # print('Attrs:', tag.attrs)
print(sum)