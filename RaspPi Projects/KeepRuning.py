import time
import subprocess as sub
total = 0

while 1:
    logFile = open("test.txt", 'w')
    print("=" * 50)
    print("it's working")
    print("=" * 50)
    sub.call(['python', 'Project 1.py'])
    print("=" * 50, file=logFile)
    print("it's working", file=logFile)
    print("=" * 50, file=logFile)
    total = total + 1
    print("it's ran", total, "times")
    print("it's ran", total, "times", file=logFile)
    logFile.close()
    time.sleep(3)
