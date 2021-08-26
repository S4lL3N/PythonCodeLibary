# =======================================================================================================
#
#        Name: Shae Allen
#        Date: 03/17/2018
#      Course: CITC 1301
#     Section: A70
# Description: This is a simple receipt generator where you ask
#  the user for what items they had for dinner, then calculate the amount
#  of the check, add tax, and print the receipt to both the console window
# and a text file.
#
#
# ======================================================================================================

import datetime

# --------Variables--------------------------------------------------------------------------------------
now = datetime.datetime.now()
soda = 2.55
water = 1.19
soup = 5.23
hamburger = 11.99
cake = 8.89
pie = 7.89
receipt = open("receipt.txt", 'w')
tax = .0925

# -----------Header--------------------------------------------------------------------------------------
# formatted to the center of 40 characters

def header():
    print("{0:^40}".format("The Happy Gizzard"))
    print("{0:^40}".format("Fine Dining"))
    print("{0:^40}".format(now.strftime("%m-%d-%Y %H:%M")))
    # --------------Write header to file-----------------------------------------------------------------
    print("{0:^40}".format("The Happy Gizzard"), file=receipt)
    print("{0:^40}".format("Fine Dining"), file=receipt)
    print("{0:^40}".format(now.strftime("%m-%d-%Y %H:%M\n")), file=receipt)

def main():
    # ---------------User Input--------------------------------------------------------------------------
    # the "if '' == ''.upper()" checks for upper case input
    drink = input("\n\tDid You have (s)soda or (w)water ?:")

    if drink == 's' or drink == drink.upper():
        drink = soda
    elif drink == 'w' or drink == drink.upper():
        drink = water
    else:
        print("Error: please enter either s or w next time.")
        main()

    meal = input("\tDid you have (s)soup or (h)hamburger ?:")

    if meal == 's' or meal == meal.upper():
        meal = soup
    elif meal == 'h' or meal == meal.upper():
        meal = hamburger
    else:
        print("Error: please enter either s or h next time.")
        main()

    dessert = input("\tDid you have (c)cake or (p)pie ?:")

    if dessert == 'c' or dessert == dessert.upper():
        dessert = cake
    elif dessert == 'p' or dessert == dessert.upper():
        dessert = pie
    else:
        print("Error: please enter either c or p next time.")
        main()

# ---------------Itemized list----------------------------------------------------------------
# ---------Write Itemized list to file--------------------------------------------------------
    # formatted right aligned 10 characters wide, and right aligned 16 characters wide to .2 decimal points
    print("\n\tItemized List:")
    print("\n\tItemized List:", file=receipt)
    if drink != water:
        print("\t{0:>10} {1:*>16.2f}".format("Soda:", soda))
        print("\t{0:>10} {1:*>16.2f}".format("Soda:", soda), file=receipt)
    else:
        print("\t{0:>10} {1:*>16.2f}".format("Water:", water))
        print("\t{0:>10} {1:*>16.2f}".format("Water:", water), file=receipt)
    if meal == soup:
        print("\t{0:>10} {1:*>16.2f}".format("Soup:", soup))
        print("\t{0:>10} {1:*>16.2f}".format("Soup:", soup), file=receipt)
    else:
        print("\t{0:>10} {1:*>16.2f}".format("Hamburger:", hamburger))
        print("\t{0:>10} {1:*>16.2f}".format("Hamburger:", hamburger), file=receipt)
    if desert == cake:
        print("\t{0:>10} {1:*>16.2f}".format("Cake:", cake))
        print("\t{0:>10} {1:*>16.2f}".format("Cake:", cake), file=receipt)
    else:
        print("\t{0:>10} {1:*>16.2f}".format("Pie:", pie))
        print("\t{0:>10} {1:*>16.2f}".format("Pie:", pie), file=receipt)

# ---------------Totals----------------------------------------------------------------------
    # formatted right aligned 12 characters wide, and right aligned 17 characters wide to .2 decimal points
    subTotal = drink + meal + dessert
    salesTax = subTotal * tax
    grandTotal = subTotal + salesTax

    print("\n\tTotals:")
    print("\t{0:>12} {1:*>17.2f}".format("Subtotal:", subTotal))
    print("\t{0:>12} {1:*>17.2f}".format("Tax:", salesTax))
    print("\t{0:>12} {1:*>17.2f}".format("Grand total:", grandTotal))

# --------------Write Totals to file---------------------------------------------------------
    print("\n\tTotals:", file=receipt)
    print("\t{0:>12} {1:*>17.2f}".format("Subtotal:", subTotal), file=receipt)
    print("\t{0:>12} {1:*>17.2f}".format("Tax:", salesTax), file=receipt)
    print("\t{0:>12} {1:*>17.2f}".format("Grand total:", grandTotal), file=receipt)

    # Closing the text file
    receipt.close()


header()
main()
