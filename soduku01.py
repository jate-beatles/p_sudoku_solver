


def solve_sudoku(puzzle):
    #sovle a 9x9 puzzle by python practice 
    #the puzzle input as list of list
    #the input puzzle fill the empty with -1

    row, col = find_empty(puzzle)
    #If fill then is fixed number
    if row is None:
        return Ture
    
    #making a guess for the empty 



def find_empty(puzzle):
    #find the index of the empty 
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c

    return None, None 



def is_valid(puzzle, guess, row, col):
    #check the validation of the guess, RETURN true/false
    row_vals = puzzle[row]
    if guess in row_vals:
        
