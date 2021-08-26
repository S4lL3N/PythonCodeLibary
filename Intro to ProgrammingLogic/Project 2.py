# ===============================================================
#
#        Name: Shae Allen
#        Date: 01/30/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program asks the user for three numbers and
# calculates the average. Then outputs the results to the console
# window.
#
# ===============================================================

# importing datetime
import datetime

# defining main function and print statements
def main():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("Name:Shae Allen")
    print("Date/Time:", datetime.datetime.today())
    print("++++++++++++++++++++++++++++++++++++++++")

# print statements formatted to the center of 40 characters
    print("{0:^40}".format("This program takes three"))
    print("{0:^40}".format("grades as inputs and then averages"))
    print("{0:^40}".format("the grades and outputs the average to"))
    print("{0:^40}".format("the console window."))
    print()
    print("{0:*^40}".format("The imput should be integer values. "))
    print()

# create three variables from user input
    gradeOne = input("Enter Grade 1:")
    gradeTwo = input("Enter Grade 2:")
    gradeThree = input("Enter Grade 3:")

# finding the averageGrade by adding all the grades together and dividing by 3
    averageGrade = (int(gradeOne) + int(gradeTwo) + int(gradeThree)) / 3
    print()

# outputs the results, formatted float values to two decimal points
    print("The average of the test scores is: ", "{0:.2f}".format (averageGrade))

main()
