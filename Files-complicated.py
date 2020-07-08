fname = input('Enter file name:')
try:
    file = open(fname)
except:
    print('No such file exists')
    quit()
count = 0
total = 0.0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')
        spac = line.find('\n', pos)  # Method to find new line immediately after pos position
        str = line[pos+2:spac]
        num = float(str)
        total = total + num
print('Average spam confidence:', total/count)