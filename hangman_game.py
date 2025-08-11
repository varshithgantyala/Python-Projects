import random
def hangman_game():

    word = random.choice(["alligator", "bear", "cat", "dolphin", "elephant", "fox", "giraffe", "horse", "iguana", "jellyfish", "kangaroo", "lion", "monkey", "newt", "octopus", "penguin", "quail", "rabbit", "snake", "tiger", "urial", "vulture", "whale", "xray","yak","zebra"])
    valiLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns = 10
    guess_made = ''

    while len(word)>0:
        main = " "
        missed = 0

        for letter in word:
            if letter in guess_made:
                main = main+letter
            else:
                main = main + "_" + " "
        if main == word:
                print(main)
                print("You win!")
                break
        print("Guess the word : ", main)
        guess = input()

        if guess in valiLetters:
            guess_made = guess_made + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turn left")
                print("Be Careful!")
                print("  --------  ")
                print("   \ O _|/  ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You lose!")
                print("The word was: ", word)
                break
name = input("Enter Your Name : ")
print("Welcome to Hangman Game, ", name)
print("Let's play Hangman!")
print("Try to guess the Animals word in less than 10 attempts.")
hangman_game()
print("Thanks for playing Hangman!")
print()    
