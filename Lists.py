fname = input('Enter the file name:')
words = list()
file = open(fname)
for line in file:
    pieces = (line.rstrip()).split()
    for element in pieces:
        # if element in words is True:
        # continue
        # else:                        Why doesn't this work?? Why are elements repeated??
        # words.append(element)
        if element not in words:
            words.append(element)

words.sort()
print(words)
