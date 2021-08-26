# open_file = open('test.txt', 'w')
# open_file.write('A string to write')
# open_file.close()

# read_file = open('test.txt', 'r')
# read_file.read()
# read_file.close()

# with open('test.txt', 'w') as open_file:
    # open_file.write("123")

    # open_file.write('shae allen')
    # open_file.close()


def file_read(fname):
    txt = open(fname)
    print(txt.read())



file_read('test.txt')


def writeToFile():

    try:

        # create a file object to write to test.txt file
        # note the "w" in the parameter list.
        myFile = open("test.txt", "w")

        print("Here is some text that I want to write out to a file", file=myFile)
        print("And {0:^40}\nhere is\n\tsome more text".format("center using string format()"), file=myFile)
        print("{0:*>20.2f}".format(12.3432), file=myFile)

        myFile.close()
    except:
        print("There was a problem with a file write operation")


def readFromFile():

    try:
        # create a file object to write to test.txt file
        # note the "r" in the parameter list.
        myFile = open("test.txt", "r")
        # read in all contents of file
        data = myFile.read()

        # print out the contents
        print("Printing contents of file:")
        print(data)

        myFile.close()
    except:
        print("There was a problem with a file read operation")


def main():
    writeToFile()
    readFromFile()




main()