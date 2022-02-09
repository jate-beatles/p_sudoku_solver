####Soduku_2
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
    if len(row)== 9:
        nrow += 1
        print("Row check: Row " + str(nrow) + " of " +str(len(row)) + " number")


#Print out puzzle with hyphen
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

print(print_puzzle(puzzle))


