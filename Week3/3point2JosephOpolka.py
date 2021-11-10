h = input("Enter Hours: ")
r = input("Enter Rate: ")
try:
    hh = float(h)
    rr = float(r)
except:
    print("Error")
    quit()

print(hh, rr)
if hh > 40:
    reg = hh * rr
    otp = (hh - 40.0) * (rr * 0.5)
    xp = reg + otp
else:
    xp = hh * rr
print("Paycheck: ", xp)
