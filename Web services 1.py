# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data
# from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_42.xml for testing

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

count = 0
total = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
tree = ET.fromstring(html)
counts = tree.findall('comments/comment')
for item in counts:
    x = int(item.find('count').text)
    count += 1
    total += x
print('Count:', count)
print('Sum:', total)



