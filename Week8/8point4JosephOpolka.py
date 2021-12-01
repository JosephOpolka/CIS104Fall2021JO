op = open('romeo.txt')
ls = []
if True:
    word = op.read()
    val = word.split()
for dup in val:
    if dup in ls:
        continue
    ls.append(dup)
    ls.sort()

print(ls)
