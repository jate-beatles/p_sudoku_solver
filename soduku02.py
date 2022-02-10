####Soduku_2
from sympy import false

puzzle = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


#Checking the input data intact as 9x9 
print("Row of the Puzzle:" + str(len(puzzle)))
nrow = 0
for row in puzzle:
    if len(row) == 9:
        nrow += 1
        print("Row check: Row " + str(nrow) + " has " +str(len(row)) + " number")


#Print out to show the puzzle with hyphen
def print_puzzle(puzzle):
    for i in range(len(puzzle)):
        if i % 3 ==0 and i != 0:
            print("- - - - - - - - - - ")
        
        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = "")
                
            if j == 8:
                print(puzzle[i][j])
            else: 
                print(str(puzzle[i][j]) + " ", end = "")
    return("")

#find the empty 
def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i,j)
    return


#check the validation of the puzzle
def valid(puzzle, num, pos):
    #pos is the [][] for the row and col val
    #checking the row of select num, puzzle[] is the row number
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False
    
    #checking the column, pos[1] is the col pos val
    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    #checking the 3x3 cube to find out
    #index the 3x3 box for each number in it, except the 0
    #set the cube index
    cube_x = pos[1] // 3
    cube_y = pos[0] // 3

    #switch the cube index to puzzle index for each num 
    for i in range(cube_y*3, cube_y*3 +3):
        for j in range(cube_x*3, cube_x*3 +3):
            if puzzle[i][j] == num and (i,j) != pos:
                return False
    
    return True


def solve(puzzle):
    #recursion
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(puzzle, i, (row, col)):
            puzzle[row][col] = i 

            if solve(puzzle):
                return True 
            puzzle[row][col] = 0
    
    return False

print(print_puzzle(puzzle))
solve(puzzle)
print("- - - - - - - - - - - - - - \n   Solved Puzzle")
print(print_puzzle(puzzle))
print("END")











# print ("puzzle[0]-----"+ str(puzzle[0]))
# print ("puzzle[0][0]-----" + str(puzzle[1][0]))

