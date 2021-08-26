import random

def header():
    print("{0:^30}".format("Shae Allen"))
    print("{0:^30}".format("Exam 1"))
    print("{0:^30}".format("CITC 1301"))


def main():
    randValue = random.randint(1, 500)
    #print("\n\tRandom Value 1:" + "${0.2f}".format(randValue))
    print("\n\tRandom Value 1:", randValue)

    if randValue >= 250:
        handleingFee = randValue * .0325
        print("\tHandling fee :", round(handleingFee, 2))
        total = randValue + handleingFee
        print("\tFor a total of:", round(total, 2))

    elif randValue >= 100:
        handleingFee = randValue * .0515
        total = randValue + handleingFee
        print("\tHandling fee :", round(handleingFee, 2))
        print("\tFor a total of:", round(total, 2))

    elif randValue <= 249:
        handleingFee = randValue * .0515
        total = randValue + handleingFee
        print("\tHandling fee :", round(handleingFee, 2))
        print("\tFor a total of:", round(total, 2))

    else:
        handleingFee = randValue * .0930
        total = randValue + handleingFee
        print("\tHandling fee :", round(handleingFee, 2))
        print("\tFor a total of:", round(total, 2))


    randValue1 = random.randint(1, 500)
    print("\n\tRandom Value 2:", randValue1)

    if randValue1 >= 250:
        handleingFee1 = randValue1 * .0325
        total1 = randValue1 + handleingFee1
        print("\tHandling fee :", round(handleingFee1, 2))
        print("\tFor a total of:", round(total1, 2))

    elif randValue1 >= 100:
        handleingFee1 = randValue1 * .0515
        total1 = randValue1 + handleingFee1
        print("\tHandling fee :", round(handleingFee1, 2))
        print("\tFor a total of:", round(total1, 2))

    elif randValue1 <= 249:
        handleingFee1 = randValue1 * .0515
        total1 = randValue1 + handleingFee1
        print("\tHandling fee :", round(handleingFee1, 2))
        print("\tFor a total of:", round(total1, 2))

    else:
        handleingFee1 = randValue1 * .0930
        total1 = randValue1 + handleingFee1
        print("\tHandling fee :", round(handleingFee1, 2))
        print("\tFor a total of:", round(total1, 2))

    grandTotal = total + total1
    print()
    print("\tGrand total is:", round(grandTotal, 2))




header()
main()
