import urllib
import urllib.parse
import urllib.request
import json
import requests



def menu():
    #print("\033[1;31;48m Bright red  \n")
    print(30 * "-", "MENU", 30 * "-")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(67 * "-")

    choice = str(input("Enter your choice [1-5]:"))

    if choice == "1":
        print("Menu 1 has been selected")
        avon()

    elif choice == "2":
        print("Menu 2 has been selected")
        frisco()

    elif choice == "3":
        print("Menu 3 has been selected")

    elif choice == "4":
        print("Menu 4 has been selected")

    elif choice == "5":
        print("Menu 5 has been selected")
        print("Goodbye!")
        exit()

    else:
        print("Wrong option selection.")
        menu()

def avon():
        mainapi = "https://query.yahooapis.com/v1/public/yql?"
        # address = "select wind from weather.forecast where woeid=2460286"
        address = "select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"avon,nc\")"
        url = mainapi + urllib.parse.urlencode({"q": address}) + "&format=json"
        json_data = requests.get(url).json()
        print("Avon,NC:")
        print(json_data)
        menu()

def frisco():
        mainapi = "https://query.yahooapis.com/v1/public/yql?"
        address = "select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"frisco,nc\")"
        url = mainapi + urllib.parse.urlencode({"q": address}) + "&format=json"
        json_data = requests.get(url).json()
        print("frisco,NC")
        print(json_data)
        menu()




menu()