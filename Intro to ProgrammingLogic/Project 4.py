# ==================================================================
#
#        Name: Shae Allen
#        Date: 02//2018
#      Course: CITC 1301
#     Section: A70
# Description: This application takes user input to convert a
# temperature to either fahrenheit or celsius.
#
#
# ==================================================================


# defining header function
def printHeader():
    # text formatted to the center
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Temperature Converter"))
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Name:Shae Allen"))
    print("{0:^40}".format("Due Date: Feb 19, 2018"))
    print("++++++++++++++++++++++++++++++++++++++++")
    print()


def main():
    # declaring user input as a string variable to choose conversion formula
    conversionFormula = str(input("Enter 1 to convert Celsius to Fahrenheit, 2 to convert Fahrenheit to Celsius:"))
    print()
    # if user input is 1 run the FahrenheitToCelsius function
    if conversionFormula == "1":
        fahrenheitToCelsius()
        print()
        restart()

    # if user input is 2  run the celsiusToFahrenheit function
    elif conversionFormula == "2":
        celsiusToFahrenheit()
        print()
        restart()

    # if user input is anything other than 1 or 2 notify user and restart main function
    else:
        print("Invalid selection!")
        print()
        main()


def celsiusToFahrenheit():
    # declaring user input as a float value for the temperature to be converted
    fahrenheit = float(input("Enter Fahrenheit temperature to convert to Celsius:"))
    # assigning the converted temperature and printing the results rounded to 2 decimal points
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius:", round(celsius, 2))

def fahrenheitToCelsius():
    # declaring user input as a float value for the temperature to be converted
    celsius1 = float(input("Enter Celsius temperature to convert to Fahrenheit:"))
    # assigning the converted temperature and printing the results rounded to 2 decimal points
    fahrenheit1 = 9 / 5 * celsius1 + 32
    print("Fahrenheit:", round(fahrenheit1, 2))

def restart():
    startOver = str(input("would you like to convert another temperature?  \nType: \"yes\" or \"no\""))
    if startOver == "yes":
        print()
        main()

    elif startOver == "no":
        print("Goodbye!")
        exit()

    else:
        print()
        print("Invalid selection!")
        print()
        restart()


printHeader()
main()







