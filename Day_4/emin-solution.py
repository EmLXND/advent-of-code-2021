import os

# find file in folder structure
input_file_name = "emin-input.txt"
input_file_path = os.path.join(os.path.dirname(__file__), input_file_name)

# read bingo boards from input file
with open(input_file_path) as file:
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


def check_for_winner(list):
    # function to check for the first board to have an empty row or column
    for index, board in enumerate(list):
        # check for an empty row
        for row in board:
            if all(value == "drawn" for value in row):
                # print(row)
                return index
            else:
                # print(row)
                pass
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
                    return index
                else:
                    pass


# read drawing order from input file, drop numbers and check for winners sequentially
file = open(input_file_path, "r")
drawing_order = file.readline().strip("\n").split(",")
for str_number in drawing_order:
    mark_number_as_drawn(str_number, list_of_boards)
    winner = check_for_winner(list_of_boards)
    if winner != None:
        # save last drawn winning number for final calculation of score
        winning_number = int(str_number)
        break

# get sums of all unmarked numbers
winning_board = list_of_boards[winner]
for row in winning_board:
    while("drawn" in row):
        row.remove("drawn")
flattened_winning_board = [int(cell) for row in winning_board for cell in row]
sum_of_unmarked_numbers = sum(flattened_winning_board)

# calculate score
score = sum_of_unmarked_numbers * winning_number
print(score)
