# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags, scan for a tag that is in a particular position
# relative to the first name in the list, follow that link and repeat the process
# a number of times and report the last name you find.
# http://py4e-data.dr-chuck.net/known_by_Fikret.html for testing
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

i = 0
j = int(input("Enter position:"))
k = int(input("Enter repetitions:"))

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
webs = list()

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print(type(tags))
for tag in tags:
    x = tag.get('href', None)
    webs.append(x)
n = webs[j - 1]
print(url)
print(n)


def website():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    webs = list()
    global n
    url = n
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        x = tag.get('href', None)
        webs.append(x)
    n = webs[j - 1]
    print(n)


while i < k - 1:
    website()
    i += 1
