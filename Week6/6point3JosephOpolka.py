def count():
    num = 0
    fruit = input("Enter a fruit: ")
    let = input("Enter letter: ")

    for letter in fruit:
        if letter == let:
            num = num + 1
    print(num)

count()
