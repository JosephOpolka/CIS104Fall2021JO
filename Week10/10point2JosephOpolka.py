fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0

dct = dict()

for line in fh:
    if not line.startswith("From "): continue
    word = line.split()
    time = word[5]
    hr = time.split(':')
    dct[hr[0]] = dct.get(hr[0], 0) + 1

for hr, count in sorted(dct.items()):
    print(hr, count)
