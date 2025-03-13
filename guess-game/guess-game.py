secret_word = "cat"
guess_word = ""
guess_count = 0
guess_limit = 3
isOut = False

while secret_word != guess_word and not(isOut):
    if guess_count < guess_limit:
        print("Cuttest animal in the world \n")
        guess_word = input("Your Guess: ")
        guess_count += 1
    else:
        isOut = True

if isOut: 
    print("Game Over")
else:
    print("Correct!")
