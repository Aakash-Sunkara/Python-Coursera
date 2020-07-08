n = int(input("Enter number of elements : "))

# 'map' is a function 
score = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

# dict.fromkeys takes items from list as keys. Since keys can't be duplicated,
# we get unique values and duplicates are removed
score = list(dict.fromkeys(score))
score.sort(reverse=True)
print('Runner up score is', score[1])
