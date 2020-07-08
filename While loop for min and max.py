largest = None
smallest = None
count = 0
total = 0.0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        val = float(num)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + val

    while largest is None or smallest is None:  # Note "is" and "None" expressions carefully
        largest = smallest = val
    if largest < val:
        largest = val
    elif smallest > val:
        smallest = val

lar = int(largest)
sma = int(smallest)

print("Maximum is", lar)
print("Minimum is", sma)
print(total, count, total / count)
