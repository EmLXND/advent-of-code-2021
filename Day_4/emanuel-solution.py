import pandas as pd

#import data
called_numbers_list = [46,79,77,45,57,34,44,13,32,88,86,82,91,97,89,1,48,31,18,10,55,74,24,11,80,78,28,37,47,17,21,61,26,85,99,96,23,70,3,54,5,41,50,63,14,64,42,36,95,52,76,68,29,9,98,35,84,83,71,49,73,58,56,66,92,30,51,20,81,69,65,15,6,16,39,43,67,7,59,40,60,4,90,72,22,0,93,94,38,53,87,27,12,2,25,19,8,62,33,75]

bingo_boards_list_of_strings = [
'84 94 24 52 44',
'96 33 74 35 13',
'60 51 41 19 95',
'50 93 27 40  1',
'67 23 37 88 85',
'',
'12 85  6 97 77',
'79 28 24 70 51',
'71 72 78 55 73',
'11 36  5 98 19',
'30 67 89 95 62',
'',
'54 38 70 29 51',
'16 19 80 96 63',
'76 23 10 30 24',
'45 81 97 82 90',
'60 94 28 11 83',
'',
'50 56 42 68 48',
' 6 70 78 22 27',
'75 11 63 24 47',
'29 99 91 73 97',
' 7 16 28 12 44',
'',
'20 62 50 36 12',
' 3 10 40  8 56',
'78 61 66 37 89',
'72 26 19 65 22',
'30 91 27  5 63',
'',
'75 91 84  0 96',
' 1 58 83 81 20',
'36  8 82 66 77',
'59 15 71 80 56',
'17 45 46 26 73',
'',
'33 71 28 10 80',
'90  0 92 30 74',
'66 46 43 88 75',
'11 36 42 67 22',
'37 79 69 17 94',
'',
'46 66  4 20 77',
'59 34 23 30 52',
'85 65 61 33 40',
'19 48 82 68 37',
'88 11 12 43 75',
'',
' 4 53 32 29  3',
' 0  6 17  5 76',
'13 67 92  2 24',
'64 57 80 42 30',
'18 85 21 65 44',
'',
'90 98 50  8 89',
'40  9 42 62 61',
'60 86 48 31 32',
'15 96 88 95  1',
'93 68 72 74 73',
'',
'75 90 96 59 95',
'84 38 26 70 73',
'23 11 63 29 48',
'28  1  4 80 55',
'15 14 67 12 61',
'',
' 1 93 54 63 56',
'61 19 20  8 95',
' 3 73 22 60 36',
'91 27 37 38 99',
'83 64 74 87 28',
'',
'13 89 95 72 37',
'10 81 47 52 88',
'56 78 50 42 73',
'38  0  5 43 55',
'77 69 74 28 94',
'',
' 7 59 76 36 43',
'48 82 57  4 83',
'22 62  1 16 11',
'37 27 54 34 87',
'95 89 85  3 44',
'',
'76  6 53 52 89',
'31 18 81 23 25',
'77 79 20 66  7',
'72 19 73 91 57',
'17 33 63 92 88',
'',
'52 51  1 19  7',
'36 46 73 37  6',
'87 77  2 56 57',
' 8 18 40 23 71',
'50 58  5 65 31',
'',
'45 86 87 12 75',
'95 20 93 72 50',
'90  1 55 13 66',
'14  3 70 97 54',
'32 26 60 11 62',
'',
'20 25  0 82 83',
' 3 14 61 34 46',
'85 58 65 76 26',
'47 15 86 81 88',
'49 90 16 42 70',
'',
'87 85 68 17 57',
'69 40 99 71 24',
'12 55 86 95 64',
'42  2  1 72  3',
'80  7 18 94 31',
'',
'27 41 21 89 46',
'57  3 18 98  4',
' 5 60 62 54 14',
'31 26 81 53 71',
'91 13 43 12 15',
'',
'66 82  9 23  8',
'52 64 79 99 29',
'21  7 39 74 70',
'50  0 89 26  5',
' 1 83 62  6 93',
'',
'64 85 74 73 11',
' 1 57  0 97 93',
'95  7 17 45 47',
'52  5 28 81 34',
'18  8 80 29 54',
'',
' 0 10 92 70 88',
'30 14 77 24 33',
'56  6 75 40 48',
'17 34 65 79 68',
'51 67 71 64  8',
'',
'36 10 94 91 34',
' 8 23  6 79 40',
' 4 44 15  0 67',
'90 97 12 26 30',
'57 93 22 99 27',
'',
'22 90 32 83 40',
'84 67 69  4 49',
'39 42 16 29 71',
'47 77 15 13 78',
'19 92 43 62 35',
'',
'50  7 86  9 33',
'93 73 51 26 46',
'91 84 67 29 56',
'69 54 74 19 35',
' 2 43 63 53 78',
'',
'85 51  4 17 90',
'21 67 24 40 99',
'10 83 84 11 48',
' 8 56 87  2  6',
' 7 30 74 35 43',
'',
'11 67 27 60 39',
'43 40 94  1 50',
'15 42 75 24 21',
'87 68 29 41 84',
'86 16 63 74  2',
'',
'84 64  7 11 50',
'54 70 40 60 86',
'67 66 58 18 98',
'85 32 91 90 75',
'81 97 74 94 28',
'',
'56 93 51 46 89',
'29 14 53 17 64',
' 9 94 82 79 62',
'81 84 58 78 90',
'95 67 37 30 44',
'',
'91 17 88 54 41',
' 5 22 37 15 63',
'36 89 34 48 49',
'11 27 83 40 80',
' 8  7 26 69 33',
'',
'77 57 52 75 18',
' 8 33 48  9 97',
'99 80 10 31 28',
'64 14 49 68 72',
'26 66 35 36 45',
'',
'81 22 65 55 39',
'32 97 18  4 23',
'61 91 60 33 40',
' 3 54 48  2 68',
'24 62 67 53 77',
'',
'86 87 78 73 75',
' 0  2 54 95 63',
'99 83 12 68 27',
'13 90 44 77 88',
'79 47 72 84  4',
'',
'30 48 23 81 93',
'36 89 79 75 43',
'54 55 29 74 92',
'71 32 51 52 62',
'13 72  6 63 65',
'',
'44 78  4 57 37',
'15 24 88 30 89',
'34 35 69 16 91',
'36 12 98 55 51',
'31 27 49 46 48',
'',
'60 32 24 98 58',
'63 14 91  4  1',
'74 69 56 65 40',
'36 77 79 28 43',
'95 31 12 88 55',
'',
'22 36 33  3 46',
'64 79 25 38 10',
' 1  5 99 48 82',
'35 96 21 50  7',
'15 88 58 27 66',
'',
'87 62 22 41 79',
'57  0 82 18 48',
'17 73 83 46 60',
'14 97  7 28 31',
'90 94 16 58 66',
'',
'21 56 79  8 54',
'35 58 25 12 22',
'27 75  7 93 86',
' 3 99  9 59 32',
'45 40 64 60 68',
'',
'96 26 19 49 28',
' 7 58 72 14 12',
'55 80  1 35 71',
'29 41 63 74 65',
'69 46 75 82 73',
'',
'57 71 64 13 56',
'31 77 95 40 66',
'80  9  7 88 49',
'73 47 82 46 75',
'23 15  1 36  2',
'',
'62 23 58  0 75',
'14 96 60 85 59',
'49 43 80 64 29',
' 5 44 24 30 54',
'78 90 98 97 38',
'',
'86 40 56 32 41',
'27 19 69 30 77',
'48 31  4 26 58',
'55 78 94 34 99',
'72 65 92 37 71',
'',
'16 23 61 65 34',
'62 88 52 10 29',
'11 77 67  2 90',
'44 30 82 32 13',
'26 53 56 93  9',
'',
'60  6 79 29 12',
'28 68 21 71 97',
' 3 24 34 63 95',
'13 52 74 18 91',
'14 64 57 94 20',
'',
'98 84 40 24 45',
'69 81  1 85 49',
'91 29 78  7 35',
' 5 20 27 93 61',
'47 95 43 39 17',
'',
'49 35 97 41 26',
'10 51 36 94 14',
'65 83 82 27 55',
'24 88 29 13 95',
'56 57 38 16 21',
'',
'98  3 62 58 45',
'67 17 81 93 19',
'86 42 10 99 51',
' 8 57 55 63 92',
'25 50 76 18  4',
'',
'39 99 67 56 30',
'41  1  7 68 70',
'37 75 29 62 50',
'61 55 16 52 15',
'84  0 73 31 33',
'',
'19  3 87 72 90',
'57 43 35  8 15',
'51 10  4 42 56',
'86 62 25 29 83',
'97 49 28 70 59',
'',
' 8 13 31 38 59',
'86 94 55 10  1',
'81 18 45 48 32',
'43 25 37 49 67',
'22 95 11 82 44',
'',
'12 87 40 76  5',
'18 43 69 98 27',
'30  4 63 20 89',
' 7 97  0  9 54',
'39 45 25 53 52',
'',
'14 32 62 54 56',
'57 66 19 99 51',
'65 41 90 94 11',
'36 10 87 83 73',
'84 82 50 95 29',
'',
' 2 92 14  4 11',
' 9 63 81 20 46',
'26 39 70 15  7',
'18 85 68 79 84',
'74 32 57 12 28',
'',
'70 59 90 17 15',
'33 16  3 41 26',
' 8 49 73 95 76',
'93 13 94 55 91',
'20 54 30 74 52',
'',
'95  8 54 84 34',
'33 24 68 14 64',
'88 42 27 10 20',
'70 40 52  6 32',
'99  9  1 72 73',
'',
'81 63 67 98 79',
'42 14 48 74  4',
'10 51  8 13 56',
'90 61  3 18 23',
'33 58 43 75 41',
'',
'93 42 68 44 53',
'26  1 21 22 64',
'56 32 30  9 35',
'63 91 29 40 47',
'99 57 11 96 15',
'',
'43 29 69 68 65',
'23 16 15 86  6',
'50 56 78  9 21',
'73 82 36  7 22',
' 8 18 37 58 95',
'',
'19 85 36 73 71',
'65 62 14 52  3',
'30 83 44 41  5',
'55 15  0 61 95',
'28 13 32 31 88',
'',
'48 92 33 50  7',
'11 47 46 35 76',
'36 37 54  2 89',
'23 63 52 69  9',
'56 20 67 14 43',
'',
'38 28 47 70 57',
' 4 85 46 97 34',
'14 94  2 35 72',
'27 58 63 68 39',
' 6 92 54 91 96',
'',
'28 96 60 89 37',
'83 77 57  5 27',
'71 67 99 91 29',
'88 10 41 19 50',
'76  9 20 14 98',
'',
'52 43 80 33  1',
'68 83 59 37 87',
'10 85 24 90 58',
'48 79 69 27 42',
'76 61 86 23  7',
'',
'72 49 51 12 43',
'73 56 83  4 27',
'48 94 38 18 32',
'14 96 36  8 13',
'87 60  5 77 42',
'',
'41 36 16 28  2',
'94 15 97 70 48',
'32 39 80 95 69',
'31 75 21  8 19',
'79 65 50 14 67',
'',
'76 67 16 49 87',
' 3 22 11 82 65',
'73 15 78 13 52',
'19 17 64  9 56',
'60 77 24 91 38',
'',
'11 56 41  8 86',
'53 38 69 62 67',
'32  6 35 24 66',
'57 84 83 49  2',
'82 88 10 28 47',
'',
'13 60 28 34 76',
'57 54 59 48 99',
'19 85 53 22 45',
' 9 69 55 32 64',
'70 15  5 71 33',
'',
'91 63  9  8 85',
'37 46 23 60 24',
'59 50 87 43  3',
'57 47 51 98 25',
'53 86  4 42 52',
'',
'19 82 11 14 89',
' 4 78 92 43  5',
'96 61 67 47 69',
'50 45 49 86 44',
'27 88 32 98 59',
'',
'83  8 33 54 16',
'30 95 23 86 27',
'44 72  5 43  2',
'76 26 28 63 81',
'24 37 45 90 73',
'',
'16 48  9 62 61',
'50 45 92 59  4',
'56 86 98  3 44',
'76 43 97 40 11',
'38 58 67 20 74',
'',
'14 75 39 44 42',
'47 80 99 57 77',
' 1 48 24 85 79',
'68 38 25 28 49',
'17 20 11 36 67',
'',
'67 59 32 19 53',
'45 26  0 35 91',
'85 80 89 51 25',
' 7 95 11 78 73',
'50  5  1 88 62',
'',
'38 91 25 80 14',
'26 96 82 52 67',
' 8 53 92 77 34',
'49 76 50 35 42',
'66 17 85 75 16',
'',
'36 63 78 73 26',
'51 28 74 57 54',
'21 27 14  2 67',
'19 69 16 40 41',
'95 45 38 70  8',
'',
'12 23 17 46 91',
'75 88 58 25  9',
'65 64 62 49 33',
'27 59 63 21 73',
'56 31 87 81  0',
'',
'14 82 79 46 51',
'32 77 11  1 99',
' 0 29 15 25 64',
'44 16 35 60 95',
'41 54 72 61 87',
'',
'58  2 13 51  1',
'29 97 98 71 36',
'66 89 50 38 62',
'87 42 79 75 76',
'37  6 77 11 72',
'',
'97 98 88 90 73',
'36 50 71 33 57',
'44  9 37 54 25',
'27 15 13 77 60',
'21 24 72 68 85',
'',
'77 58 45 95 32',
'38 79 84 56 90',
' 1 70 24 88 12',
' 7 91 98  9 18',
'93 89 37 81 25',
'',
'53 34 44 59 46',
'61 42 89 37 15',
'23 30 43  3 55',
'49  6 60 79 50',
'77 10 92 36 17',
'',
'60 14 58 49 19',
' 9 87 80 76  3',
'81 62 66 38 50',
'53 28 69 12 64',
'98 83 72 34 85',
'',
'38 30 52 43 24',
'75 29 57  4  3',
'97 72 94 41 19',
'80 90 39  9 20',
' 6 91 10 44 67',
'',
'51 43 76 64 42',
'16 56 46 82 99',
'55 72 35 39 65',
'66 86 93 23 34',
'31 84  9 96 74',
'',
'64 68 14  2 97',
'88 22 99 23 28',
' 5 41 11 47 63',
'81 17 10 27 89',
'24 36  0 58 86',
'',
'20 34  1 89 36',
'86 15 79 30 17',
'96 31  4 50 16',
'92 23 61 12 99',
'60 65 91 13 76',
'',
'41 67 90 27 78',
'85 48 40 57 19',
'43 36 30 11 68',
'16 91 76 74 81',
'97 39 86 75 80',
'',
'94 92 54 14 60',
'31 17 39 77 73',
'11 12 52 49 40',
'63 96 68 35 71',
'98 75 37 65 44',
'',
' 3 97 59 72 85',
'14 55 96 87 28',
'47 63 91 81 50',
'68 79  9 35 37',
'49 10  1 24 20',
'',
'42 66 54 29 95',
'47 28 81 14 68',
'37 15 22 58 13',
'49 36 90 72  5',
'74 71 88 34 70',
'',
'34 65 39  6 86',
'80 43  8 14 27',
'72 45  0 25 23',
'50  2 13 41 26',
'64 18  9 69 35',
'',
'36 43  4  3 90',
'69 47 95 10 65',
' 6 56 30 13 22',
'55 50 63 99 76',
'54 92 51 96 23',
'',
'56  4 52 37 98',
'84 49 95 33 85',
'34 87 75 15 91',
'14 68 13 24 97',
'59 58 10 90 93',
'',
'26 63 36 68 39',
'47 79 33 25  8',
'91 52 11 59 93',
'50 67 96 34  6',
'20 54 41 89  3',
'',
'63 59 34 62 74',
'84 76 88 54  8',
'15 61 60  7 77',
'22 55 18 80 37',
'90  2 94 91 70',
'',
'23 12 16 11 50',
'59 27 58 32 35',
'92 42 75 19 70',
'31 88 28 30 95',
'17 72 80 39 91',
'',
'38 46 18 54 76',
'25 22 47 10 11',
'63 29 74 71 92',
'75 98  0 65  4',
'87 14 13 64 12']


#create a data frame containing all boards
bingo_boards_df = pd.DataFrame([], columns = ["A", "B", "C", "D", "E"])     #at this point the data frame is empty
#A, B, C, D and E represent the five columns of each board

#fill the data frame with the board data from the bingo boards list of strings
for i in bingo_boards_list_of_strings:

    current_df_length = len(bingo_boards_df)   #the length is 0 for the very first run of this loop
    data = i.split(" ")                        #we split the values in each row (string) of a board

    for j in data:
        if j == "": data.remove(j)             #we remove potential space values, since we are only interested in the actual numbers

    if len(i) == 0:     #this indicates that we are currently between two boards since there is an empty string between boards, therefore we will do nothing
        pass            #nothing
    else:
    bingo_boards_df.loc[current_df_length] = data   #else we append the row at the end the board data frame

print(bingo_boards_df)  # we see a 500x5 data frame with all boards integrated


#which row will be the first full row?
list_for_winning_row = []                               #we write in this list how many numbers must be called to fill a row, and we do this for each row, so that the list should contain 100x5 elements at the end
bingo_boards_df_length = len(bingo_boards_df)           #this length should be 100x5=500 for 100 boards with columns of length=5

for row in range(bingo_boards_df_length):               #loop for each row
    called_numbers_to_fill_row = 5                      #initialize with 5 as best possible score (= 5 numbers had to be called, to fill the row)
    current_row_list = list(bingo_boards_df.loc[row])   #row we are currently looking at is converted to a list

    for element in current_row_list:                    #we check each element of the row (which was just converted to a list)
        if called_numbers_list.index(int(element)) > called_numbers_to_fill_row:    #is the element/number called "later" than the current value of called_numbers_to_fill_row
            called_numbers_to_fill_row = called_numbers_list.index(int(element))    #if yes, then update called_numbers_to_fill_row => by doing this, we find out the index of the last number that was called for each row!

    list_for_winning_row.append(called_numbers_to_fill_row)                         #then we add this index to the list, which containts the index of the last call for each row

minimum_to_fill_row = min(list_for_winning_row)                                     #the smallest index shows the "best performing" row
index_of_minimum = list_for_winning_row.index(minimum_to_fill_row)                  #the index of the minimum can be used to derive, which board contains the "best performing" row
winning_board_row =  (index_of_minimum // 5) + 1                                    #floor division by 5 and adding 1 returns the "nth" board, which was the winner by row
print("The fewest amount of numbers called to fill a row was " + str(minimum_to_fill_row+1) + " numbers, with "
+ str(list_for_winning_row.count(minimum_to_fill_row)) + " row(s) that was filled at this time." +
" Therefore one winning board (by row) is the board number " + str(winning_board_row) + ".")

#now which column on which bingo board will be the first full column?
list_for_winning_column = []                        #again we write in this list how many numbers must be called to fill a column, and we do this for each column, so that the list should contain 100x5 elements at the end
column_length = 5                                   #define the column length per board

for column in range(5):                             #we loop through all 5 columns of the boards
    beginning_of_current_column = 0                 #this is a counter, which points to the beginning of the column we are currently looking at in the following loop
    ending_of_current_column = 5                    #this is a counter, which points to the ending of the column we are currently looking at in the following loop

    for board in range(int(bingo_boards_df_length/column_length)):  #the data frame length divided by column length per board equals the number of boards in the data frame => we loop through each board for the current column
        called_numbers_to_fill_column = 5           #initialize with 5 as best possible score (= 5 numbers had to be called, to fill the column)
        current_column_list = list(bingo_boards_df.iloc[beginning_of_current_column:ending_of_current_column, column])  #we define a list, which contains the numbers of the column we are currently looking at

        for element in current_column_list:         #we check each element of the column (which was just converted to a list)
            if called_numbers_list.index(int(element)) > called_numbers_to_fill_column:     #this is similar to the row analysis we already run at this time
                called_numbers_to_fill_column = called_numbers_list.index(int(element))

        list_for_winning_column.append(called_numbers_to_fill_column)
        beginning_of_current_column += 5            #update the counter after each analyzed board-column
        ending_of_current_column +=5                #update the counter after each analyzed board-column

minimum_to_fill_column = min(list_for_winning_column)                           #the smallest index shows the "best performing" column
index_of_minimum = list_for_winning_column.index(minimum_to_fill_column)        #the index of the minimum can be used to derive, which board contains the "best performing" column

if index_of_minimum < 100:                          #if the index_of_minimum is between 0 and 99...
    winning_board_column = index_of_minimum + 1     #... this number + 1 equals the winning board of the 100 boards...
else:                                               #...else...
    winning_board_column = int(str(index_of_minimum)[1:]) + 1   #...the last two digits of index_of_minimum + 1 equal the winning board of the 100 boards

print("The fewest amount of numbers called to fill a column was " + str(minimum_to_fill_column+1) + " numbers, with "
+ str(list_for_winning_column.count(minimum_to_fill_column)) + " columns that was filled at this time." +
" Therefore one winning board ist the board number " + str(winning_board_column) + ".")

#depending on if a row was filled first, or a column was filled first, we derive the "winning number" and the winning board
if minimum_to_fill_row < minimum_to_fill_column:        #if fow was filled first
    final_winning_board = winning_board_row
    final_winning_board_last_number = called_numbers_list[minimum_to_fill_row]
elif minimum_to_fill_row == minimum_to_fill_column and winning_board_row == winning_board_column:   #if a row and column was filled at the same time for the same board
    final_winning_board = winning_board_row
    final_winning_board_last_number = called_numbers_list[minimum_to_fill_row]
elif minimum_to_fill_row == minimum_to_fill_column and not winning_board_row == winning_board_column:   #a row was filled at the same time as a column was filled on a different board
    print("There are two winning boards: " + winning_board_row + " and " + winning_board_column)
else:
    final_winning_board = winning_board_column              #else a column was filled first
    final_winning_board_last_number = called_numbers_list[minimum_to_fill_column]
print("The winner is board " + str(final_winning_board))

#calculate score
all_numbers_on_final_winning_board_list = []                                    #initialize by empty list
first_row_of_winning_board = (final_winning_board-1)*5                          #where in the data frame is the winning board located?
last_row_of_winning_board = first_row_of_winning_board + column_length          #where in the data frame is the winning board located?

for row in range(first_row_of_winning_board, last_row_of_winning_board):        #add the numbers on the winning board to all_numbers_on_final_winning_board_list row by row
    current_row_data = list(bingo_boards_df.loc[row])
    print(current_row_data)
    all_numbers_on_final_winning_board_list.extend(current_row_data)
    print(all_numbers_on_final_winning_board_list)

numbers_not_called_on_final_winning_board = all_numbers_on_final_winning_board_list     #initialize numbers_not_called_on_final_winning_board by adding all numbers on the board
sum = 0                                                                                 #initialize the sum of all numbers not called

for i in range(len(all_numbers_on_final_winning_board_list)):                           #check for each number on the winning board, if it was called at the time the bingo game was terminated => if yes remove it
    current_value = all_numbers_on_final_winning_board_list[i]
    if int(current_value) in called_numbers_list[0:called_numbers_list.index(final_winning_board_last_number)+1]:
        #numbers_not_called_on_final_winning_board.remove(current_value)
        print(current_value + " called")
        #print(numbers_not_called_on_final_winning_board)
    else:                                                                              #else add it to the sum
        print(current_value + " not called")
        sum += int(current_value)

sum_of_not_called_numbers = sum
score = sum_of_not_called_numbers * final_winning_board_last_number

print("The score is: " + str(score))

