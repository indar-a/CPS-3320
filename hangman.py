from random import choice

word = choice(["Binary", "Bitmap", "Driver", "Editor", "Google", 
        "Laptop", "Parser", "Router", "Python", "Update"])

guessed = []
wrong = []

tries = 6

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess the a letter:", out)
    print(tries, "chances left")

    guess = input()

    if guess in guessed or guess in wrong:
        print("This word has been guessed already", guess)
    elif guess in word:
        print("GREAT JOB!")
        guessed.append(guess)
    else:
        print("BAD GUESS!")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("GREAT JOB!", word)
else:
    print("You didn't get", word)
