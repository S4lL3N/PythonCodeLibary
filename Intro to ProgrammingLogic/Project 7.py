# =======================================================================================================
#
#        Name: Shae Allen
#        Date: 03/22/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program processes EDI (Electronic Data Interchange) files into a production report
#
#
# ======================================================================================================


def header():
    # -----Formatted to the center of 80 characters------------------------------------------------------------
    print("{0:^80}".format("Production Report"))
    print("{0:^80}".format("=" * 80))
    # -------Formatted Right aligned 20 characters wide--------------------------------------------------------
    print("{0:>20}{1:>20}{2:>20}{3:>20}".format("Part", "Total", "Houston Qty", "Columbus Qty"))
    print("{0:^80}".format("-" * 80))


def main():
    # --------Variables--------------------------------------------------------------------------------------
    v10xTotal = 0
    v10xTX = 0
    v10xOH = 0

    v11xTotal = 0
    v11xTX = 0
    v11xOH = 0

    v12xTotal = 0
    v12xTX = 0
    v12xOH = 0

    try:
        # --------Open text file for reading----------------------------------------------------------------
        edi = open("edi.txt", 'r')
        # --------Loop For Reading every line in the text file----------------------------------------------
        for line in edi:
            # -----Breaking up the string at every : --------------------------------------------------------
            partList = line.split(":")
            # print(partList[0], partList[1], partList[2]) # test code
            #
            if partList[0] == "V10X":
                v10xTotal += int(partList[1])
                if partList[2] == "Houston":
                    v10xTX += int(partList[1])
                if partList[2] == "Columbus":
                    v10xOH += int(partList[1])

            if partList[0] == "V11X":
                v11xTotal += int(partList[1])
                if partList[2] == "Houston":
                    v11xTX += int(partList[1])
                if partList[2] == "Columbus":
                    v11xOH += int(partList[1])

            if partList[0] == "V12X":
                v12xTotal += int(partList[1])
                if partList[2] == "Houston":
                    v12xTX += int(partList[1])
                if partList[2] == "Columbus":
                    v12xOH += int(partList[1])

        print("{0:>20}{1:>20}{2:>20}{3:>20}".format("V10X", v10xTotal, v10xTX, v10xOH))
        print("{0:>20}{1:>20}{2:>20}{3:>20}".format("V11X", v11xTotal, v11xTX, v11xOH))
        print("{0:>20}{1:>20}{2:>20}{3:>20}".format("V12X", v12xTotal, v12xTX, v12xOH))

    except:
        print("Error reading the file.")
    # ------Closing the text file-----------------------------------------------------------------------------
    edi.close()


header()
main()