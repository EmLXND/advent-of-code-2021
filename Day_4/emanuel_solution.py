import pandas as pd
from emanuel_input import called_numbers_list, bingo_boards_list_of_strings


# create a data frame containing all boards
# at this point the data frame is empty
bingo_boards_df = pd.DataFrame([], columns=["A", "B", "C", "D", "E"])
# A, B, C, D and E represent the five columns of each board

# fill the data frame with the board data from the bingo boards list of strings
for i in bingo_boards_list_of_strings:

    # the length is 0 for the very first run of this loop
    current_df_length = len(bingo_boards_df)
    data = i.split(" ")  # we split the values in each row (string) of a board

    for j in data:
        if j == "":
            # we remove potential space values, since we are only interested in the actual numbers
            data.remove(j)

    if len(i) == 0:  # this indicates that we are currently between two boards since there is an empty string between boards, therefore we will do nothing
        pass  # nothing
    else:
        # else we append the row at the end the board data frame
        bingo_boards_df.loc[current_df_length] = data

print(bingo_boards_df)  # we see a 500x5 data frame with all boards integrated


# which row will be the first full row?
list_for_winning_row = []  # we write in this list how many numbers must be called to fill a row, and we do this for each row, so that the list should contain 100x5 elements at the end
# this length should be 100x5=500 for 100 boards with columns of length=5
bingo_boards_df_length = len(bingo_boards_df)

for row in range(bingo_boards_df_length):  # loop for each row
    # initialize with 5 as best possible score (= 5 numbers had to be called, to fill the row)
    called_numbers_to_fill_row = 5
    # row we are currently looking at is converted to a list
    current_row_list = list(bingo_boards_df.loc[row])

    # we check each element of the row (which was just converted to a list)
    for element in current_row_list:
        # is the element/number called "later" than the current value of called_numbers_to_fill_row
        if called_numbers_list.index(int(element)) > called_numbers_to_fill_row:
            # if yes, then update called_numbers_to_fill_row => by doing this, we find out the index of the last number that was called for each row!
            called_numbers_to_fill_row = called_numbers_list.index(
                int(element))

    # then we add this index to the list, which containts the index of the last call for each row
    list_for_winning_row.append(called_numbers_to_fill_row)

# the smallest index shows the "best performing" row
minimum_to_fill_row = min(list_for_winning_row)
# the index of the minimum can be used to derive, which board contains the "best performing" row
index_of_minimum = list_for_winning_row.index(minimum_to_fill_row)
# floor division by 5 and adding 1 returns the "nth" board, which was the winner by row
winning_board_row = (index_of_minimum // 5) + 1
print("The fewest amount of numbers called to fill a row was " + str(minimum_to_fill_row+1) + " numbers, with "
      + str(list_for_winning_row.count(minimum_to_fill_row)) + " row(s) that was filled at this time." +
      " Therefore one winning board (by row) is the board number " + str(winning_board_row) + ".")


# now which column on which bingo board will be the first full column?
list_for_winning_column = []  # again we write in this list how many numbers must be called to fill a column, and we do this for each column, so that the list should contain 100x5 elements at the end
column_length = 5  # define the column length per board

for column in range(5):  # we loop through all 5 columns of the boards
    # this is a counter, which points to the beginning of the column we are currently looking at in the following loop
    beginning_of_current_column = 0
    # this is a counter, which points to the ending of the column we are currently looking at in the following loop
    ending_of_current_column = 5

    # the data frame length divided by column length per board equals the number of boards in the data frame => we loop through each board for the current column
    for board in range(int(bingo_boards_df_length/column_length)):
        # initialize with 5 as best possible score (= 5 numbers had to be called, to fill the column)
        called_numbers_to_fill_column = 5
        # we define a list, which contains the numbers of the column we are currently looking at
        current_column_list = list(
            bingo_boards_df.iloc[beginning_of_current_column:ending_of_current_column, column])

        # we check each element of the column (which was just converted to a list)
        for element in current_column_list:
            # this is similar to the row analysis we already run at this time
            if called_numbers_list.index(int(element)) > called_numbers_to_fill_column:
                called_numbers_to_fill_column = called_numbers_list.index(
                    int(element))

        list_for_winning_column.append(called_numbers_to_fill_column)
        # update the counter after each analyzed board-column
        beginning_of_current_column += 5
        ending_of_current_column += 5  # update the counter after each analyzed board-column

# the smallest index shows the "best performing" column
minimum_to_fill_column = min(list_for_winning_column)
# the index of the minimum can be used to derive, which board contains the "best performing" column
index_of_minimum = list_for_winning_column.index(minimum_to_fill_column)

if index_of_minimum < 100:  # if the index_of_minimum is between 0 and 99...
    # ... this number + 1 equals the winning board of the 100 boards...
    winning_board_column = index_of_minimum + 1
else:  # ...else...
    # ...the last two digits of index_of_minimum + 1 equal the winning board of the 100 boards
    winning_board_column = int(str(index_of_minimum)[1:]) + 1

print("The fewest amount of numbers called to fill a column was " + str(minimum_to_fill_column+1) + " numbers, with "
      + str(list_for_winning_column.count(minimum_to_fill_column)) + " columns that was filled at this time." +
      " Therefore one winning board ist the board number " + str(winning_board_column) + ".")


# depending on if a row was filled first, or a column was filled first, we derive the "winning number" and the winning board
if minimum_to_fill_row < minimum_to_fill_column:  # if fow was filled first
    final_winning_board = winning_board_row
    final_winning_board_last_number = called_numbers_list[minimum_to_fill_row]
# if a row and column was filled at the same time for the same board
elif minimum_to_fill_row == minimum_to_fill_column and winning_board_row == winning_board_column:
    final_winning_board = winning_board_row
    final_winning_board_last_number = called_numbers_list[minimum_to_fill_row]
# a row was filled at the same time as a column was filled on a different board
elif minimum_to_fill_row == minimum_to_fill_column and not winning_board_row == winning_board_column:
    print("There are two winning boards: " +
          winning_board_row + " and " + winning_board_column)
else:
    final_winning_board = winning_board_column  # else a column was filled first
    final_winning_board_last_number = called_numbers_list[minimum_to_fill_column]
print("The winner is board " + str(final_winning_board))


# calculate score
all_numbers_on_final_winning_board_list = []  # initialize by empty list
# where in the data frame is the winning board located?
first_row_of_winning_board = (final_winning_board-1)*5
# where in the data frame is the winning board located?
last_row_of_winning_board = first_row_of_winning_board + column_length

# add the numbers on the winning board to all_numbers_on_final_winning_board_list row by row
for row in range(first_row_of_winning_board, last_row_of_winning_board):
    current_row_data = list(bingo_boards_df.loc[row])
    print(current_row_data)
    all_numbers_on_final_winning_board_list.extend(current_row_data)
    print(all_numbers_on_final_winning_board_list)

# initialize numbers_not_called_on_final_winning_board by adding all numbers on the board
numbers_not_called_on_final_winning_board = all_numbers_on_final_winning_board_list
sum = 0  # initialize the sum of all numbers not called

# check for each number on the winning board, if it was called at the time the bingo game was terminated => if yes remove it
for i in range(len(all_numbers_on_final_winning_board_list)):
    current_value = all_numbers_on_final_winning_board_list[i]
    if int(current_value) in called_numbers_list[0:called_numbers_list.index(final_winning_board_last_number)+1]:
        # numbers_not_called_on_final_winning_board.remove(current_value)
        print(current_value + " called")
        # print(numbers_not_called_on_final_winning_board)
    else:  # else add it to the sum
        print(current_value + " not called")
        sum += int(current_value)

sum_of_not_called_numbers = sum
score = sum_of_not_called_numbers * final_winning_board_last_number

print("The score is: " + str(score))
