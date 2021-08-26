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

def header():
    print("\t{0:^30}".format("-" * 30))
    print("\t{0:^30}".format("Blackjack"))
    print("\t{0:^30}".format("-" * 30))

def main():
    # ------------------------------------------------------------------------------------------------------------------
    hiddenCard = random.randint(1, 10)
    visibleCard = random.randint(1, 10)
    hand = hiddenCard + visibleCard
    dealerhiddenCard = random.randint(1, 10)
    dealervisibleCard = random.randint(1, 10)
    dealerHand = dealerhiddenCard + dealervisibleCard
    # ------------------------------------------------------------------------------------------------------------------
    name = str(input("\n\tEnter you name: "))
    print("\thello,", name, "and welcome to python Blackjack!")
    print("\tYour hand value is:", hand)
    # ------------------------------------------------------------------------------------------------------------------
    while True:
        hitOrStay = str(input("\tWould you like to (h)it or (s)tay?"))
        if hitOrStay == "s":
            if dealerHand < 21 and dealerHand < hand:
                dealerHitCard = random.randint(1, 10)
                print(hitCard, "hit card")
                dealerHand += dealerHitCard
                print("you hand value is:", dealerHand, "\n")

            if hand > dealerHand:
                print("\tthe dealer had", dealerHand)
                print("you win!!!")
                exit()
            if hand < dealerHand:
                print("\tthe dealer had", dealerHand, "you lose!!!")
                exit()
            break
        if hitOrStay == "h":
            hitCard = random.randint(1, 10)
            print(hitCard, "hit card")
            hand += hitCard
            print("you hand value is:", hand, "\n")

            if hand > 21:
                print("bust you lose!!!")
                exit()
            if hand == 21:
                print("blackjack!!! you win")
                exit()
            continue


header()
main()

#print(hiddenCard, "hidden card")
#print(visibleCard,"visable card")
#print(dealerHand, "dealer hand")
#print(dealervisibleCard, "dealer visable")
#print(dealerhiddenCard, "dealer hidden")