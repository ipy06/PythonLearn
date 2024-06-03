#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a sudoku board validation script
It asks the user to input the sudoku board and then it runs checks
to determint if the board entered is valid
"""

print("Welcome to the sudoku validation program.\n")
print("Please enter the sudoku puzzle as a 9x9 grid of numbers below row by row:")
puzzle = []
for i in range(9):
    row = input()
    puzzle.append(row)

# rows
for row in puzzle:
    for i in range(1,10):
        if row.count(str(i)) > 1:
            print("Not valid beacause row"  , puzzle.index(row) , "has a duplicate value of", i)
            exit()

# columns
for i in range(9):
    column = [row[i] for row in puzzle]
    for j in range(1,10):
        if column.count(str(j)) > 1:
            print("Not valid beacause column", i , "has a duplicate value of", j)
            exit()


# 3x3 boards
for i in range(0,9,3):
    for j in range(0,9,3):
        board = [puzzle[x][y] for x in range(i,i+3) for
                 y in range(j,j+3)]
        for k in range(1,10):
            if board.count(str(k)) > 1:
                print("Not valid beacause the 3x3 board at position " + str(i) + str(j), end=" ")
                print("has a duplicate value of", k)
                exit()
print("The sudoku puzzle is valid.")


# Tests

# Sample input:
# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672

# Output: The sudoku puzzle is valid

# Sample Input:
# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671

# Output: The sudoku puzzle is valid