# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data
# from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:
# http://py4e-data.dr-chuck.net/comments_42.json for testing

from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urlopen(url, context=ctx).read().decode()
info: object = json.loads(html)

i = 0
tot = 0
a = len(info['comments'])
print('User count:', a)

while i < a:
    y = info['comments'][i]['count']
    tot += y
    i += 1
print('Sum:', tot)
