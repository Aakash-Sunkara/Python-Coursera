han = open('lists complicated.txt')
count = 0
for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian
    if len(wds) < 1:
        continue
    if wds[0] != 'From:':
        continue
    count = count + 1
    print(wds[1], count)
    # guardian a bit stronger, because the above guardian leaves the sentence if it has only one word
    if len(wds) < 3:
        continue
    # guardian in a compound statement, order of statements is very important below
    if len(wds) < 3 or wds[0] != 'From:':
        continue
