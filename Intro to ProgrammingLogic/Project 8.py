# ======================================================================================================================
#
#        Name: Shae Allen
#        Date: 03/28/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program takes X number of grades, then finds the highest, lowest, and the average of the grades
# entered.
#
# ======================================================================================================================
# Empty list variable
gradeList = []

# ------------------------------------------->USER INPUT<---------------------------------------------------------------
# Asks the user for the length of the list of grades. Then loops through the input of the grades, appending them to the
# list variable "gradeList". All input fields are formatted with two tabs. If a entered grade is not in range (1-100) it
# exits the program, and if there is a "ValueError" it exits the program.
def main():
    try:
        listLength = int(input("\t\tHow many values will you enter?"))
        print()
        for listEntry in range(listLength):
            total = str(listEntry + 1)
            number = float(input("\t\tEnter grade " + total + ':'))
            if number > 100 or number < 0:
                print("{0:^0}\n{1:^0}".format("Error...", "Enter a integer between 1 and 100 next time."))
                exit()
            gradeList.append(number)
    except (IndexError, ValueError):
        print("{0:^0}\n{1:^0}".format("Error...", "Enter a integer next time."))
        exit()
# ------------------------------->FINDING THE HIGHEST AND LOWEST GRADE<-------------------------------------------------
    # Assigns the first integer in the list to the highest and lowest value, then loops through the rest of the list.
    # If the following integer is bigger, it takes the "highestValue" place. If the following integer is smaller it
    # takes the "smallestValue" place.
    highestValue = gradeList[0]
    smallestValue = highestValue
    for grade in gradeList:
        if grade < smallestValue:
            smallestValue = grade
        if grade > highestValue:
            highestValue = grade
# ---------------------------------------->AVERAGING THE GRADES<--------------------------------------------------------
    # Adds all the integers in the list "gradeList", and divides by the chosen list length "listLength".
    gradesTotal = sum(gradeList)
    average = gradesTotal / listLength
# ---------------------------------------------->OUTPUT<----------------------------------------------------------------
    # Outputs the results, formatted right aligned, 28 characters wide. The average is formatted to two decimal points.
    print("\n{0:>28} {1:>0.2f}".format("Highest grade recorded:", highestValue))
    print("{0:>28} {1:>0.2f}".format("Lowest grade recorded:", smallestValue))
    print("{0:>28} ${1:>0.2f}".format("Average Grade:", average))
# ----------------------------------------------------------------------------------------------------------------------


main()