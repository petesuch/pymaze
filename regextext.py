#!/usr/bin/python3.7

import re

fn = open("demofile.txt", "r")
regex = r"(?P<fullLine>.{70,80}\s)"
subst = "\\g<fullLine>\\n"

for line in fn:
    # specify number of replacements by changing 4th argument
    result = re.sub(regex, subst, line, 0)
    if result:
        print (result)

