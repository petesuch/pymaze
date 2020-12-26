#!/usr/bin/python3.7

import sys
import re

def main(argv):
    try:
        inFile = argv[0]
        outFile = argv[1]
    except:
        print ('catinFile.py <inFile> <outFile')
        sys.exit(2)
    print ('Arguments Given: ', argv)
    print ('Displaying Contents of: ', inFile)
    try:
        inF = open(inFile, "r")
        outF= open(outFile,"a")
    except:
        print ('File Not Found; File Must exist')
        print ('catinFile.py <inFile>')
        sys.exit(2)

    str = ()
    regex = r"(?P<fullLine>.{74,88}\s)"
    subst = "\\g<fullLine>\\n"

    for line in inF:
        result = re.sub(regex, subst, line, 0)
        if result:
            print(result)
            outF.write(result)

    inF.close()
    outF.close()

if __name__ == "__main__":
    main(sys.argv[1:])

