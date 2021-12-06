board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
def print_board():
    print(board[0])
    print(board[1])
    print(board[2])
print_board()
player = 1
while True:
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

