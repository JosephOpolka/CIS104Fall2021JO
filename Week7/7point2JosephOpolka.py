# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

numCount = 0
tot = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        numCount = numCount + 1
        pos = line.find(":")
        xy = line[pos+1: ]
        val = float(xy)
        tot = (tot + val)
        continue


#print("Average spam confidence: ", av)
print(numCount, tot/numCount)
