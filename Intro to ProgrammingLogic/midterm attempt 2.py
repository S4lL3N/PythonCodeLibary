import random

def header():
    print("{0:^30}".format("Shae Allen"))
    print("{0:^30}".format("Exam 1"))
    print("{0:^30}".format("CITC 1301"))


randomNumber = random.randint(1, 500)
randomNumber1 = random.randint(1, 500)
tier1 = .0325
tier2 = .0515
tier3 = .0930


if randomNumber >= 250 or randomNumber1 >= 250:
    handlingFee = randomNumber * tier1
    handlingFee1 = randomNumber1 * tier1

elif randomNumber >= 100 or randomNumber1 >= 100:
    handlingFee = randomNumber * tier2
    handlingFee1 = randomNumber1 * tier2

elif randomNumber <= 249 or randomNumber1 <= 249:
    handlingFee = randomNumber * tier2
    handlingFee1 = randomNumber1 * tier2

else:
    handlingFeelingFee = randomNumber * tier3
    handlingFee1 = randomNumber1 * tier3

total = randomNumber + handlingFee
total1 = randomNumber1 + handlingFee1
grandTotal = total + total1

def main():
    print("\n\tRandom Value 1: $", randomNumber + .00)
    print("\tHandling fee : $", round(handlingFee, 2))
    print("\tFor a total of : $", round(total, 2))
    print("\n\tRandom Value 2: $", randomNumber1 + .00)
    print("\tHandling fee : $", round(handlingFee1, 2))
    print("\tFor a total of: $", round(total1, 2))
    print("\n\tFor a grand total of: $", round(grandTotal, 2))
# print("${1:.2}".format("\n\tFor a grand total of: $",grandTotal)

header()
main()