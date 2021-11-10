def computergrade(g) :

    if g >= 0.90:
        print("A")
    elif g >= 0.80:
        print("B")
    elif g >= 0.70:
        print("C")
    elif g >= 0.60:
        print("D")
    elif g < 0.60:
        print("F")
    else:
    	print("error")

score = input("Enter Score: ")
g = float(score)

a = computergrade(g)
