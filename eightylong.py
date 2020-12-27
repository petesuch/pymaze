#!/usr/bin/python3.7
#
#   eightylong.py
#
#   roughly breaks a text file without newlines to about 80 characters
#   per line.  Useful for breaking up Kindle content so that it is more easily edited
#   with your favorite editor.
#
#   The 70-84 count can be modified to suit your needs.


import sys
import re

def main(argv):
    try:
        inFile = argv[0]
        outFile = argv[1]
    except:
        print ('eightylong.py <inFile> <outFile>jj')
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
    regex = r"(?P<fullLine>.{70,84}\s)"
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
