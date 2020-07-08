sh = input("Enter hours: ")
try:
    h = float(sh)  # try and except is used when we don't want the code to show traceback error
    # like an insurance policy, if the result turns out to be okay, then fine
    # else, it will go to the result embedded in except and hence doesn't blow up
except:
    print("Error, please enter numeric values only")
    quit()
sr = input("Enter rate: ")
try:
    r = float(sr)
except:
    print("Error, please enter numeric values only")
    quit()

if h > 40:
    pay = 40 * r + (h - 40) * r * 1.5
else:
    pay = h * r
print(pay)
