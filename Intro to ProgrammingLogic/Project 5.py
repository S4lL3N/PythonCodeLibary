# ==================================================================
#
#        Name: Shae Allen
#        Date: 02/20/2018
#      Course: CITC 1301
#     Section: A70
# Description: This is a number guessing game. prompts user to
# guess a random number between 1 and 10. Application uses if,elif and
# else conditionals and exceptions(try and except).
#
#
# ==================================================================

import random


# defining header function
def printHeader():
    # text formatted to the center
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Guess Secret Number"))
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Name:Shae Allen"))
    print("{0:^40}".format("Due Date: Feb 26, 2018"))
    print("++++++++++++++++++++++++++++++++++++++++")
    print()


def main():
    try:
        print("\tGuess a number 1-10\n")
        # assigning a random integer between 1 and 10 to a variable
        randomNumber = random.randint(1, 10)
        # print(randomNumber)  #to test if working todo comment out
        # assigning user input as a integer variable
        userGuess = int(input("\tEnter your guess:"))

        # conditionals
        # if user guesses the random number print correct and exit
        if userGuess == randomNumber:
            print("\n\tCorrect!!!")
            exit()
        # if user guesses a integer out of bounds print error and directions then rerun the main function
        elif userGuess < 1:
            print("\n\tERROR...")
            print("\tThe number you entered was out of range: Enter 1-10 next time.\n")
            main()

        elif userGuess > 10:
            print("\n\tERROR...")
            print("\tThe number you entered was out of range: Enter 1-10 next time.\n")
            main()
        # if user guesses wrong show what the number was and rerun the main function
        else:
            print("\n\tSorry, The number was:", randomNumber, "\n\tTry Again\n")
            main()
    # try and except: if the application has a value error print directions and rerun the main function
    except ValueError:
        print("\n\tERROR...")
        print("\tSorry, you must enter a valid integer: Enter 1-10 next time.\n")
        main()

printHeader()
main()

