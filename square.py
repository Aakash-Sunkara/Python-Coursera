z = int(input('Enter no of test cases:'))
a = int(input('Enter no of cubes:'))
i = 0
side = list()
while i < a:
    b = int(input('Enter side of cubes in order:'))
    side.append(b)
    i += 1
j = 0
while j < int(a / 2):
    if side[j] or side[a - j - 1] < side[j + 1]:
        print('No')
        break
