def isValidSudoku(board):
    # checking rows
    for row in board:
        if not isValidSudokuList(row):
            return False
    
    
    #checking columns
    for i in range(len(board)):
        column = []
        for j in range(len(board)):
            if j < len(board) and i < len(board):
                num = board[j][i]
                column.append(num)

        if not isValidSudokuList(column):
            return False
    
    #checking 3xs squares

    for i in range(0,len(board),3):
        for j in range (0,len(board),3):
            if not isValidSudoku3Square(board,i,j):
                return False    
    return True





def isValidSudokuList(listOfNums): # checks for duplicated in list

    is_valid = True
    for i in range(len(listOfNums)):
        num = listOfNums[i]
        for nextnum in listOfNums[i+1:]:
            if num != "." and num == nextnum:
                return False

    
    return is_valid


def isValidSudoku3Square(board,x,y): # checks for duplicate nums i 3x3 square
    listNums = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if j < len(board) and i < len(board):
                num = board[i][j]
                listNums.append(num)                
    
    if isValidSudokuList(listNums):
        return True
    else:
        return False


list1 = ["0",".",".","1",".","5",".",".","."]

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


#print(isValidSudoku3Square(board, 3, 0))

#print (isValidSudokuList(board[8]))

print (isValidSudoku(board))