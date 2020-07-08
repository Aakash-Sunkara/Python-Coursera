fname = input('Enter the file name:')
file = open(fname)
count = 0
one = list()
hr = dict()
lst = list()
for line in file:
    if line.startswith('From'):
        if line.__contains__('2008'):
            lines = line.split()
            time = lines[5]
            var = time.split(':')
            hours = var[0]
            one.append(hours)
for hour in one:
    hr[hour] = hr.get(hour, 0) + 1
for key, var in hr.items():
    newtup = (key, var)
    lst.append(newtup)
lst = sorted(lst)
for key, var in lst:
    print(key, var)
