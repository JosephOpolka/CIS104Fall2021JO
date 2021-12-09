fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0

lst = list()

for line in fh:
    if line.startswith("From "):
        word = line.split()
        lst.append(word[1])

mail = dict()
for adr in lst:
    at = adr.split("@")
    mail[at[1]] = mail.get(at[1], 0) + 1

print(mail)
