ls = ['A','B','C','D','E','F','G','H','I']

def middle(ls):
    print(ls[1:-1])

def chop(ls):
    del ls[0]
    del ls[-1]
    print(ls)
    return None

print("Original list:", ls)

middle(ls)
chop(ls)
