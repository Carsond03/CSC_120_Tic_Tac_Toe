import sqlite3
connection = sqlite3.connect("my.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS game(winner text)''')
connection.commit()
connection.close()
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
def print_board():
    print(board[0])
    print(board[1])
    print(board[2])
def check_mark():
    for i in range(0, 3, 1):
        for c in range(0, 3, 1):
            if board[i][c] == "-":
                return True
    return False
def check_win():
    for r in range(0, 3, 1):
        if board[r][0] == "X" and board[r][1] == "X" and board[r][2] == "X":
            print("Player 1, is the winner")
            cursor.execute("insert into game values('player 1')")
            return True
    for r in range(0, 3, 1):
        if board[r][0] == "O" and board[r][1] == "O" and board[r][2] == "O":
            print("Player 2, is the winner")
            cursor.execute("insert into game values('player 2')")
            return True
    for c in range(0, 3, 1):
        if board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X":
            print("player 1, is the winner")
            cursor.execute("insert into game values('player 1')")
            return True
    for c in range(0, 3, 1):
        if board[0][c] == "O" and board[1][c] == "O" and board[2][c] == "O":
            print("player 2, is the winner")
            cursor.execute("insert into game values('player 2')")
            return True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player 1, is the winner")
        cursor.execute("insert into game values('player 1')")
        return True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1, is the winner")
        cursor.execute("insert into game values('player 1')")
        return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player 2, is the winner")
        cursor.execute("insert into game values('player 2')")
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player 2, is the winner")
        cursor.execute("insert into game values('player 2')")
        return True
    return False
print_board()
player = 1
while True:
    if check_mark() == False:
        print("no more moves on the board")
        if check_win() == False:
            print("draw")
            break

        break
    print("player {}, make your move".format(player))
    while True:
        while True:
            a = input("Enter row nos(0-2):")
            if a == "0" or a == "1" or a == "2":
                a = int(a)
                break
            else:
                print("Invalid Entry")
        while True:
            b = input("Enter col nos(0-2):")
            if b == "0" or b == "1" or b == "2":
                b = int(b)
                break
            else:
                print("Invalid Entry")
        if board[a][b] == "-":
            break
        else:
            print("Invalid Entry")
    if player == 1:
        board[a][b] = "X"
    else:
        board[a][b] = "O"
    print_board()
    if player == 1:
        player = 2
    else:
        player = 1
    if check_win() == True:
        break
connection.commit()
connection.close()



