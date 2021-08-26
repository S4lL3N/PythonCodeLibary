# ======================================================================================================================
#
#        Name: Shae Allen
#        Date: 04/02/2018
#      Course: CITC 1301
#     Section: A70
# Description: Exam 2
#
#
# ======================================================================================================================

def main():
    buildingList = []
    maxLevel = 0
    minLevel = 0
    try:

        numberOfBuildings = int(input("\tEnter the number of buildings:"))
        if numberOfBuildings <= 0:
            print("Invalid Entry")
            exit()

        for entry in range(numberOfBuildings):
            totalCount = str(entry + 1)
            numberOfFloors = int(input("\tEnter the number of floors for building " + totalCount + ":"))
            buildingList.append(numberOfFloors)
            maxLevel = buildingList[0]
            minLevel = maxLevel

            for building in buildingList:
                if building > maxLevel:
                    maxLevel = building
                if building < minLevel:
                    minLevel = building

    except ValueError:
        print("Invalid Entry")
        exit()

    totalFloors = sum(buildingList)
    total = len(buildingList)
    averageFloors = round(totalFloors / total, 2)
    strAvgFloors = str(averageFloors)

    print("\n{0:>30}{1:<20}".format("Maximum number of floors:", maxLevel))
    print("{0:>30}{1:<20}".format("Minimum number of floors:", minLevel))
    print("{0:>30}{1:<20}".format("Total amount of floors:", totalFloors))
    print("{0:>30}{1:<20}".format("Average number of floors:", strAvgFloors))


main()







