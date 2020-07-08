sh = input("Enter hours: ")
try:
    h = float(sh)
except:
    print("Error, please enter numeric values only")
    quit()

sr = input("Enter rate: ")
try:
    r = float(sr)
except:
    print("Error, please enter numeric values only")
    quit()

def computepay(a, b):
    a = h
    b = r
    if a > 40:
        pa = 40 * b + (a - 40) * b * 1.5
    else:
        pa = a * b
    return pa


pay = computepay(h, r)

print("Pay", pay)
