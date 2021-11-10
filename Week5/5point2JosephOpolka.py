min = None
max = 0
while True :
    sval = input('Enter a number: ')

# done loop
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
# done loop

# maximum and minimum
    if fval > max:
        max = fval

    if min is None:
        min = fval
    elif fval < min:
        min = fval

print("Maximum is ", max)
print("Minimum is ", min)
