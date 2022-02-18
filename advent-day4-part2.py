bingoNum = [91,17,64,45,8,13,47,19,52,68,63,76,82,44,28,56,37,2,78,48,32,58,72,53,9,85,77,89,36,22,49,86,51,99,6,92,80,87,7,25,31,66,84,4,98,67,46,61,59,79,0,3,38,27,23,95,20,35,14,30,26,33,42,93,12,57,11,54,50,75,90,41,88,96,40,81,24,94,18,39,70,34,21,55,5,29,71,83,1,60,74,69,10,62,43,73,97,65,15,16]




file = open('bingo.txt', 'r')
data = file.read()
file.close()
bingoData = data.split()

boards = []

new_board = []
new_line = []
board_index = 0
while (board_index < len(bingoData)):
    new_line.append(bingoData[board_index])
    if (len(new_line) == 5):
        new_board.append(new_line)
        new_line = []
    if (len(new_board) == 5):
        boards.append(new_board)
        new_board = []
    board_index += 1




num_lines = len(bingoData) / 5
num_boards = num_lines / 5
num_boards = int(num_boards)

for search in range(len(bingoNum)):
    for board_index in range(num_boards):
        for line_index in range(5):
            for num_index in range(5):
                if (boards[board_index][line_index][num_index] == str(bingoNum[search])):
                    print(boards[board_index][line_index][num_index])
                    boards[board_index][line_index][num_index] = "*"

    for board_index in range(num_boards):
        for line_index in range(5):
            count = 0
            for num_index in range(5):
                if (boards[board_index][line_index][num_index] == "*"):
                    count += 1
                else:
                    break
                if (count == 5):
                    print("bingo board: " + str(board_index))
                    for i in range(5):
                        for j in range(5):
                            boards[board_index][i][j] = "o"
                        
                    

    for board_index in range(num_boards):
        for line_index in range(5):
            count = 0
            for num_index in range(5):
                if (boards[board_index][num_index][line_index] == "*"):
                    count += 1
                else:
                    break
                if (count == 5):
                    print("bingo board: " + str(board_index))
                    for i in range(5):
                        for j in range(5):
                            boards[board_index][i][j] = "o"
