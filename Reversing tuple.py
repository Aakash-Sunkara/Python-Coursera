# Tough to modify a tuple. Hence convert it to a list, modify and then make it a tuple again
z = input('Enter the word:')
y = list()
a = len(z)
c = int(a/2)
i = 0
while i < a:
    y.append(z[a-i-1])
    i += 1
x = tuple(y)
print(x)
