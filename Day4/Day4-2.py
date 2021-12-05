# load puzzle input
with open("Day4\BingoBoards.txt", "r") as f:
    data = f.readlines()

# get the picked numbers
all_picked_numbers = [int(i) for i in data[0].split(",")]

# remove newline elements
data = [i.rstrip("\n") for i in data if i != "\n"]

# split list every 5 elements
def split_every_5(long_list: list) -> list:
    new_list = []
    for i in range(0, len(long_list), 5):
        new_list.append(long_list[i:i + 5])
    return new_list


boards_grouped = split_every_5(data[1:])

# convert flattened boards into 2d lists
def make_board(flattened_board: list) -> list:
    board = []
    for i in range(5):
        better_row = [int(i) for i in flattened_board[i].replace(
            "  ", " ").lstrip(" ").split(" ")]
        board.append(better_row)
    return board


bingo_boards = [make_board(i) for i in boards_grouped]

# check if the board won vertically
def check_vertically(board: list, numbers_so_far: list) -> bool:
    for column in range(5):
        this_column = [board[a][column] for a in range(5)]
        if all([i in numbers_so_far for i in this_column]):
            return True
    return False

# check if the board won horizontally
def check_horizontally(board: list, numbers_so_far: list) -> bool:
    for row in range(5):
        if all([i in numbers_so_far for i in board[row]]):
            return True
    return False

# check if the board won diagonally
def check_diagonally(board: list, numbers_so_far: list) -> bool:
    diagonal_a = [board[i][i] for i in range(5)]
    if all([i in numbers_so_far for i in diagonal_a]):
        return True
    diagonal_b = [board[i][4 - i] for i in range(5)]
    if all([i in numbers_so_far for i in diagonal_b]):
        return True
    return False

# check if the board won given the previous 3 conditions
def did_board_win(board: list, numbers_so_far: list) -> bool:
    if check_vertically(board, numbers_so_far) or check_horizontally(board, numbers_so_far) or check_diagonally(board, numbers_so_far):
        return True
    return False

# figure out which bingo board will win last
def run_game(boards: list, number: list) -> list:
    picked_numbers_so_far = []
    current_num = 0
    while len(boards) >= 1:
        picked_numbers_so_far.append(number[current_num])
        for board in boards:
            if did_board_win(board, picked_numbers_so_far):
                boards.remove(board)

        current_num += 1
    return board, picked_numbers_so_far


# calculate the score of the bingo board
def get_board_score(board: list, numbers_so_far: list) -> int:
    score = 0
    for row in range(5):
        for column in range(5):
            if board[row][column] not in numbers_so_far:
                score += board[row][column]
    final_score = score * numbers_so_far[-1]
    return final_score


losing_board, numbers_so_far = run_game(bingo_boards, all_picked_numbers)

score = get_board_score(losing_board, numbers_so_far)
print(score)
