# ==================================================================
#
#        Name: Shae Allen
#        Date: 02/05/2018
#      Course: CITC 1301
#     Section: A70
# Description: This application takes user input to calculate the
#  height of a flagpole.
#
# ==================================================================

# importing the math library
import math

# defining header function
def showHeader():
    # printing strings formatted to the center
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Calculate Flagpole Height"))
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Name:Shae Allen"))
    print("{0:^40}".format("Due Date: Feb 9, 2018"))
    print("++++++++++++++++++++++++++++++++++++++++")
    print()

# defining the main function
def main():
    # declaring variables from user input, casting as floating point values,
    degrees = float(input("\tEnter the angle in Degrees to the top of the flagpole:"))
    # converting degrees to radians using the math function
    radians = math.radians(degrees)
    distance = float(input("\tEnter the distance in feet to the base of the flagpole:"))
    height = float(input("\tEnter the height of the person:"))
    print()
    # calculating the the height rounded to 2 decimal points
    print("{0:>34}".format("The height of the flagpole is:"), (round(distance * math.tan(radians) + height, 2)), "Feet")

# calling the defined functions
showHeader()
main()