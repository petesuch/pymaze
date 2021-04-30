# printArray.py

varx = 20
vary = 20
spaces =3

def printArray(ls, x, y):
    for i in range(y):
        print("\n")
        for j in range(x):
            print(ls[i][j], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(varx-1))

maze = (

["A","X","X","X","X","X","X","X","X","X","xxx","X","X","X","X","X","X","X","X","B"],

["O","X","X","X","X","X","X","X","X","O","O","O","O","O","X","O","O","O","X","O"],

["O","X","O","X","X","O","X","O","X","O","O","O","X","X","X","O","O","O","X","O"],

["O","X","O","O","X","O","X","O","X","X","O","O","X","O","O","O","O","O","X","O"],

["O","X","O","O","X","O","X","X","O","X","O","O","X","X","X","X","X","O","X","O"],

["O","X","O","O","X","O","X","O","X","X","X","O","O","O","X","O","O","O","X","O"],

["O","X","O","X","O","X","X","X","X","O","X","O","O","O","X","O","O","O","X","O"],

["O","X","X","O","X","O","X","O","X","O","X","X","X","X","O","O","X","X","X","O"],

["O","O","X","O","O","O","O","O","X","O","O","O","O","O","X","X","X","O","X","O"],

["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O","X","O"],

["O","X","O","O","X","X","X","X","X","O","X","X","X","O","X","X","X","O","X","O"],

["O","X","X","X","O","X","X","X","X","O","X","O","O","O","X","O","X","O","X","O"],

["O","X","X","X","X","O","X","X","X","O","X","O","X","O","X","O","X","O","X","O"],

["O","X","X","X","X","X","O","X","X","O","X","X","X","O","X","O","O","O","X","O"],

["O","X","X","X","X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","O"],

["O","X","X","X","X","X","X","O","X","O","X","O","X","O","X","O","O","O","X","O"],

["O","X","X","X","X","X","X","O","X","X","X","O","X","O","X","O","O","O","X","O"],

["O","X","X","X","X","X","X","X","X","O","O","O","X","O","X","O","O","O","X","O"],

["O","X","X","X","X","X","X","X","X","O","O","O","X","O","X","X","X","X","X","O"],

["C","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","Z"]

)
"""
solved = "NO"
for j in range(20):
    print("j: ", j)
    if maze[0][j] == "xxx":
        solved = "YES"
        if solved == "YES":
            break
"""

printArray(maze,varx, vary)


