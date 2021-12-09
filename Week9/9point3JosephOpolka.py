fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0

dct = dict()

for line in fh:
    if line.startswith("From "):
        word = line.split()
        dct[word[1]] = dct.get(word[1], 0) + 1

print(dct)
