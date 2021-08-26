# ======================================================================================================================
#
#        Name: Shae Allen
#        Date: 04/14/2018
#      Course: CITC 1301
#     Section: A70
# Description: This is a blackjack game.
#
# ======================================================================================================================
import random

dealerCards = []
playerCards = []
bank = [20]


# ----------------------------------------------------------------------------------------------------------------------
def header():
    print("\t{0:^30}".format("-" * 30))
    print("\t{0:^30}".format("Blackjack"))
    print("\t{0:^30}".format("-" * 30))
    name = str(input("\n\tEnter you name: "))
    print("\tHello ", name+",", " Welcome To Python Blackjack!")


# ----------------------DEAL CARDS--------------------------------------------------------------------------------------
def main():
    while len(dealerCards) != 2:
        dealerCards.append(random.randint(1, 10))
    while len(playerCards) != 2:
        playerCards.append(random.randint(1, 10))


# ------------------------BET-------------------------------------------------------------------------------------------
    while sum(bank) > 0:
        print("\n\t{0:>0}""${1:<}".format("You have: ", sum(bank)))
        bet = int(input("\tEnter your bet:"))
        pot = bet * 2
        if bet > sum(bank):
            print("\tInsufficient Funds")
            main()
        if sum(bank) <= 0:
            print("\tInsufficient Funds")
            exit()
        if sum(bank) > 0 and sum(bank) >= bet:
            break
    bank.append(-bet)
    # print(sum(bank))  # <-------------------------------------------------------------------- for testing
    # print(bank)


# ------------------------PLAYER HAND-----------------------------------------------------------------------------------
    print("\n\tYour hand value is:", sum(playerCards))
    # print(playerCards) # for testing


# ----------------------HIT OR STAY-------------------------------------------------------------------------------------
    while sum(playerCards) < 21:
        hitOrStay = str(input("\tWould you like to (h)it or (s)tay?"))

        # ----------HIT-------------------------------------------------------------------------------------------------
        if hitOrStay == "h":
            playerCards.append(random.randint(1, 10))
            # print(playerCards) # for testing
            print("\n\tYour hand value is:", sum(playerCards), "\n")

        if sum(playerCards) > 21:
            print("\t{0:*^30}".format("You busted"))
            print("\t{0:$^30}".format("Dealer Won!"))
            print("\t{0:$^30}".format(-bet))
            break

        if sum(playerCards) == 21:
            print("\t{0:$^30}".format("Blackjack!"))
            print("\n\t{0:$^30}".format("You won!"))
            print("\t{0:$^30}".format(bet))
            bank.append(pot)
            break

        # -------STAY---------------------------------------------------------------------------------------------------
        if hitOrStay == "s":
            # ----------DEALER HIT--------------------------------------------------------------------------------------
            while sum(playerCards) > sum(dealerCards) and sum(dealerCards) <= 17:
                dealerCards.append(random.randint(1, 10))
                print("\n\t{0:*^30}".format("The Dealer HIT"))
                print("\n\tDealer hand value:", sum(dealerCards))
                # print(dealerCards)     # <--------------------------------------------------------todo comment out

            if sum(dealerCards) == 21:
                print("\n\t{0:$^30}".format("Blackjack!"))
                print("\n\t{0:$^30}".format("Dealer Won!"))
                print("\t{0:$^30}".format(-bet))
                break

            if sum(dealerCards) > 21:
                print("\t{0:*^30}".format("Dealer busted"))
                print("\n\t{0:$^30}".format("You won!"))
                print("\t{0:$^30}".format(bet))
                bank.append(pot)
                break

            if sum(playerCards) > sum(dealerCards):
                print("\n\t{0:$^30}".format("You won!"))
                print("\t{0:$^30}".format(bet))
                bank.append(pot)
                break

            if sum(playerCards) < sum(dealerCards):
                print("\n\t{0:$^30}".format("Dealer Won!"))
                print("\t{0:$^30}".format(-bet))
                break

            if sum(playerCards) == sum(dealerCards):
                print("\n\t{0:$^30}".format("TIE!"))
                print("\t{0:$^30}".format(bet))
                bank.append(bet)
                break

# -------------RESULTS--------------------------------------------------------------------------------------------------
    print("\n\tPlayer results:", sum(playerCards))
    print("\tDealer results:", sum(dealerCards))

    if sum(bank) <= 0:
        print("\n\tyou ran out of funds!")
        exit()
    if sum(bank) > 0:
        print("\t{0:>0}""${1:<0}".format("New Balance: ", sum(bank)))
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