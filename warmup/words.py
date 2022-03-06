user_input = input("Please provide word")
file = open("linux.words", "r")
for x in file:
    if user_input.casefold() in x.casefold():
        print(x)
