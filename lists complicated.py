fname = input('Enter the file name:')
file = open(fname)
count = 0
for line in file:
    if line.startswith('From:'):
        lines = line.split()
        print(lines[1])
        count = count + 1
cont = str(count)
print('There were ' + cont + ' lines in the file with From as the first word')
