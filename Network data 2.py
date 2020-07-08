# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_42.html for testing

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

count = 0
total = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')  # Change the word in single quotes and magic happens
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    x = int(tag.contents[0])
    count += 1
    total += x
    print('Attrs:', tag.attrs)
print(count)
print(total)
