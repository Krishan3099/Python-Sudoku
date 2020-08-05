sodoku = [
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


def solve(board):
    found = findBlank(board)

    if not found:
        return True
    else:
        row, col = found

    for i in range(1,10):
        if checkValid(board, i, found):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def checkValid(board, input, pos):
    # Check the entire row
    for i in range(len(board[0])):
        if board[pos[0]][i] == input and pos[1] != i:
            return False

    # Check the entire column
    for i in range(len(board)):
        if board[i][pos[1]] == input and pos[0] != i:
            return False

    # Check the entire square
    square_x = pos[1] // 3
    square_y = pos[0] // 3

    for i in range(square_y *3, square_y*3+3):
        for j in range(square_x *3, square_x*3+3):
            if board[i][j] == input and pos != (i,j):
                return False
    
    return True

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
            


def findBlank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row col

    return None

printBoard(sodoku)
print("-----------------------")
solve(sodoku)
printBoard(sodoku)