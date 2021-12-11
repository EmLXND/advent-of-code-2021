# read bingo boards from input file
input_file = "emin_input.txt"
with open(input_file) as file:
    list_of_rows = []
    for index, line in enumerate(file):
        # skip first two lines
        if index > 1:
            if line != "\n":
                line = line.replace("\n", "")
                row = line.split(" ")
                while("" in row):
                    # remove empty strings which are generated because sometimes there are two spaces between two numbers
                    row.remove("")
                list_of_rows.append(row)


def divide_chunks(list, n):
    # Split 5-sized chunks from list_of_rows to get a list of boards (which are 5x5)
    for i in range(0, len(list), n):
        yield list[i:i + n]


list_of_boards = list(divide_chunks(list_of_rows, 5))


def mark_number_as_drawn(str_number, list):
    # function to drop drawn numbers from all boards until a board is empty
    for board in list:
        for row in board:
            for index, num in enumerate(row):
                if num == str_number:
                    row[index] = "drawn"


def get_winner(list):
    winning_board_indices = []
    first_winning_board = None
    winning_index = None
    # function to check for the first board to have an empty row or column,
    # drops that board from the list
    for index, board in enumerate(list):
        if board == "won":
            continue
        # check for an empty row
        row_won = False
        for row in board:
            if all(value == "drawn" for value in row):
                row_won = True
                if first_winning_board == None:
                    first_winning_board = board
                winning_board_indices.append(index)
                break
            else:
                pass
        # if row has won, board is dropped, no need to check columns
        if row_won == True:
            continue
        # transform columns into lists and check for an empty column
        transformed_board = []
        number_of_columns = 5
        for column_index in range(number_of_columns):
            column = []
            for row_index, row in enumerate(board):
                column.append(row[column_index])
            transformed_board.append(column)
        for column in transformed_board:
            if all(value == "drawn" for value in column):
                if first_winning_board == None:
                    first_winning_board = board
                winning_board_indices.append(index)
                break
            else:
                pass
    for index in winning_board_indices:
        list[index] = "won"
    return first_winning_board


# read drawing order from input file, drop numbers and check for winners sequentially
file = open(input_file, "r")
drawing_order = file.readline().strip("\n").split(",")

first_winner = None
last_winner = None
for index, str_number in enumerate(drawing_order):
    mark_number_as_drawn(str_number, list_of_boards)
    winner = get_winner(list_of_boards)
    # save the first winner
    if winner != None:
        # save the board which wins first
        if first_winner == None:
            first_winner = winner
            first_winning_number = int(str_number)
        # and keep saving the last board to win to know which board would win last :)
        last_winner = winner
        last_winning_number = int(str_number)
    if len(list_of_boards) == 0:
        break


def get_sum_of_unmarked_numbers(board):
    # get sums of all unmarked numbers
    for row in board:
        while("drawn" in row):
            row.remove("drawn")
    flattened_winning_board = [int(cell)
                               for row in board for cell in row]
    sum_of_unmarked_numbers = sum(flattened_winning_board)
    return sum_of_unmarked_numbers


# calculate score for winning board (1st half of task)
first_winner_score = get_sum_of_unmarked_numbers(
    first_winner) * first_winning_number
print("first winning board score:", first_winner_score)

# now on to losing board (= board to win last) score (2nd half of task)
last_winner_score = get_sum_of_unmarked_numbers(
    last_winner) * last_winning_number
print("last winning board score:", last_winner_score)
