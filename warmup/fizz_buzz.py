# Mateusz Labun
for x in range(1, 100):  # numbers 1-100
    if (x % 3 == 0 and x % 5 == 0):  # If number multiples of 3 and 5
        print("FizzBuzz")
    elif (x % 3 == 0):  # If number multiples of 3
        print("Fizz")
    elif (x % 5 == 0):  # If number multiples of 5
        print("Buzz")
    else:  # Any other case
        print(x)
