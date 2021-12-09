text = open('words.txt')
dct = dict()

for line in text:
    val = line.split()
    for wrd in val:
        dct[wrd] = dct.get(wrd, 0) + 1

print(dct)
