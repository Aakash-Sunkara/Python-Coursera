def grade():
    num = input("Please enter your marks: ")
    try:
        x = float(num)
    except:
        print("Please enter numeric values only")
        grade()  # Try writing in such a way that program restarts itself in case of failure
    if x > 1 or x < 0:
        print("Enter values within 0 to 1 only")
    elif x >= 0.9:
        print('A')
    elif x >= 0.8:
        print('B')
    elif x >= 0.7:
        print('C')
    elif x >= 0.6:
        print('D')
    else:
        print('F')
grade()