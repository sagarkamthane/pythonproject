for i in range(101):
    if i%3 == 0:
        if i%5 == 0:
            print(f"{i} FizzBuzz")
        else:
            print(f"{i} Fizz")
    elif i%5 == 0:
        print(f"{i} Buzz")

