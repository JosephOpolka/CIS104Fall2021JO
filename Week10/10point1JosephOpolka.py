lar = None
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

dct = dict()
larg = 0

for line in fh:
    if line.startswith("From "):
        word = line.split()
        dct[word[1]] = dct.get(word[1], 0) + 1
for word, dct in dct.items():
    if lar is None or dct > lar:
        lar = dct
        larg = word

print(larg, lar)
