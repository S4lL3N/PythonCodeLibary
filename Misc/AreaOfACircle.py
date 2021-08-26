# =====================================================
#        name: shae allen
#      course: citc 1301
#     section: A70
#        Date: 2/26/18
# description: the program takes user input to calculate the
# area of a circle using either the radius or the diameter.
#
# ======================================================

import math

def header():
    print("****************************************")
    print("{0:^40}".format("Study For Midterm"))
    print("****************************************")
    print("{0:^40}".format("Name: Shae Allen"))
    print("{0:^40}".format("Date:2/26/18"))
    print("****************************************")

def main():
    userChoice = str(input("\tFind the area of a circle \n\tfor radius Enter 1.\n\tfor diameter enter 2.\n enter E to exit"))

    if userChoice == "1":
        calcArea()
        main()
    elif userChoice == "2":
        clacArea1()
        main()
    elif userChoice == "E" or userChoice == "e":
        exit()
    else:
        print("invalid selection\n Enter either 1 or 2 next time")
        main()

def calcArea():
    radius = float(input("Enter a radius:"))
    area = math.pi * math.pow(radius, 2)
    print("the area is:", round(area, 2))

def clacArea1():
    diameter = float(input("Enter a diameter:"))
    radius1 = diameter / 2
    area1 = math.pi * math.pow(radius1, 2)
    print("the area is:", round(area1, 2))


header()
main()

