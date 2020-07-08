
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

total = 0
count = 0
fname = open('ch 11 actual data.txt')
for line in fname:
    y = re.findall('[0-9]+', line)
    if len(y) > 0:
        for num in y:
            x = int(num)
            count += 1
            total += x
print("No.of values are", count)
print("Their sum is", total)
