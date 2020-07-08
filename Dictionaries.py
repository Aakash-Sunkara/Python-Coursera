fname = input("Enter file name:")
file = open(fname)
mailsdict = dict()
mailslist = list()
for line in file:
    if not line.startswith("From:"):
        continue
    lines = line.split()
    mailslist.append(lines[1])
bigmail = None
bigcount = None
for mail in mailslist:
    mailsdict[mail] = mailsdict.get(mail, 0) + 1
for mail, count in mailsdict.items():
    if bigcount is None or count > bigcount:
        bigmail = mail
        bigcount = count
print(bigmail, bigcount)
