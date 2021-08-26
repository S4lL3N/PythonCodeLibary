# ======================================================================================================================
#
#        Name: Shae Allen
#        Date: 04/11/2018
#      Course: CITC 1301
#     Section: A70
# Description: This is a blackjack game.
#
# ======================================================================================================================
import random

dealerCards = []
playerCards = []

# ----------------------------------------------------------------------------------------------------------------------
def header():
    print("\t{0:^30}".format("-" * 30))
    print("\t{0:^30}".format("Blackjack"))
    print("\t{0:^30}".format("-" * 30))
    name = str(input("\n\tEnter you name: "))
    print("\thello,", name, "and welcome to python Blackjack!")

# ----------------------DEAL CARDS--------------------------------------------------------------------------------------
def main():
    while len(dealerCards) != 2:
        dealerCards.append(random.randint(1, 10))
    while len(playerCards) != 2:
        playerCards.append(random.randint(1, 10))

    print("\tYour hand value is:", sum(playerCards))
    # print(playerCards) # for testing
# ----------------------HIT OR STAY-------------------------------------------------------------------------------------
    while sum(playerCards) < 21:
        hitOrStay = str(input("\tWould you like to (h)it or (s)tay?"))
        # ----------HIT-------------------------------------------------------------------------------------------------
        if hitOrStay == "h":
            playerCards.append(random.randint(1, 10))
            # print(playerCards) # for testing
            print("\tyou hand value is:", sum(playerCards), "\n")

        if sum(playerCards) > 21:
            print("\t{0:*^30}".format("You busted"))
            print("\t{0:$^30}".format("Dealer Won!!!"))
            break

        if sum(playerCards) == 21:
            print("\t{0:$^30}".format("Blackjack!!!"))
            break
        # -------STAY---------------------------------------------------------------------------------------------------
        if hitOrStay == "s":
            if sum(playerCards) > sum(dealerCards):
                print("\n\t{0:$^30}".format("You won!!!"))
                break
            if sum(playerCards) < sum(dealerCards):
                print("\n\t{0:$^30}".format("Dealer Won!!!"))
                break
# -------------RESULTS--------------------------------------------------------------------------------------------------
    print("\n\tPlayer results:", sum(playerCards))
    print("\tDealer results:", sum(dealerCards))
    # ---------PLAY AGAIN-----------------------------------------------------------------------------------------------
    playAgain = str(input("\n\tWould you like to play again? 'y' or 'n' "))

    if playAgain == "y":
        dealerCards.clear()
        playerCards.clear()
        main()
    else:
        exit()

header()
main()
