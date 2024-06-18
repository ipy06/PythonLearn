"""
Program to count the frequency of alphabetic characters in a file and write the results to a histogram file.

The program prompts the user to enter a file name, and then reads the file line by line. It counts the frequency of each alphabetic character (ignoring case) and stores the results in a dictionary.

The dictionary is then sorted by value in descending order, and the results are written to a new file with a ".hist" extension. Each line of the output file contains a character and its frequency, separated by "->".

Example:
    Input file: "example.txt"
    Output file: "example.txt.hist"

    Contents of "example.txt.hist":
        a->5
        b->3
        c->2
        ...
"""
from os import strerror

try:
    input_file = input("Please enter the file name: ")
except KeyboardInterrupt as e:
    print("\nProgram interrupted by user, Bye!")
    exit(0)
except ValueError:
    print("Invalid input, please restart the program and try again.")

dict_letters = {}

try:
    stream = open(input_file, 'rt')
except IOError as e:
    print("Could not open file: ", strerror(e.errno))
    exit(0)

line = stream.readline()
while line != '':
    for char in line:
        if char != ' ' and char.isalpha():
            char = char.lower()
            if char not in dict_letters:
                dict_letters[char] = 1
            else:
                dict_letters[char] += 1
    line = stream.readline()
stream.close()

stream = open(input_file + ".hist", "wt")
for letter in sorted(dict_letters, key = lambda x: dict_letters[x], reverse=True):
    count = dict_letters[letter]
    stream.write(letter + "->" + str(count) + "\n")


