fruit = input("Enter a fruit: ")
length = len(fruit)
while length > 0:
    letter = fruit[length - 1]
    print(letter)
    length = length - 1
print('done')
