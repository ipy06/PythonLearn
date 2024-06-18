""" 
Reads a file containing student data, processes the data, and prints 
the student scores in alphabetical order.

The file is expected to have a specific format, with each line 
containing a student's name, surname, and score separated by tabs. 
The program handles errors such as empty files, invalid line 
formats, and I/O errors.

It uses custom exception classes StudentsDataException, BadLine, 
and FileEmpty to handle specific types of errors.

The program prompts the user to enter the file name, reads the file, 
and stores the student data in a dictionary. It then prints the student 
scores in alphabetical order, with each score being the sum of all scores 
for that student.

Parameters: prof_file (str): The file name entered by the user.

Returns: None

Raises: FileEmpty: If the file is empty. BadLine: If a line in the file 
has an invalid format. IOError: If an I/O error occurs while reading the file. 
Exception: If any other error occurs. 
"""

from os import strerror

# Define a custom exception class for students' data-related errors
class StudentsDataException(Exception):
    pass

# Define a subclass of StudentsDataException for bad line errors
class BadLine(StudentsDataException):
    def __init__(self, message):
        # Initialize the exception with a custom error message
        self.message = message
        super().__init__(self.message)

# Define a subclass of StudentsDataException for file empty errors
class FileEmpty(StudentsDataException):
    def __init__(self, message):
        # Initialize the exception with a custom error message
        self.message = message
        super().__init__(self.message)

# Prompt the user to enter the file name for Prof. Jekyll's data
prof_file = input("Please enter Prof.Jekyll's file name: ")

# Initialize an empty dictionary to store student names and scores
name_and_score = {}

try:
    # Open the specified file in read text mode
    data = open(prof_file, 'rt')
    
    # Read the first line of the file and split it into columns using tabs as separators
    line = data.readline().split("\t")
    
    # Check if the file is empty (i.e., the first line is empty)
    if len(line) == 0:
        # Raise a FileEmpty exception if the file is empty
        raise FileEmpty("File is empty")
    
    # Process each line in the file
    while line[0] != '':
        # Check if the line has exactly 3 columns (name, surname, score)
        if len(line) != 3:
            # Raise a BadLine exception if the line format is invalid
            raise BadLine("Bad line: " + "".join(line))
        
        # Extract the student's name and score from the line
        name = line[0].strip() + " " + line[1].strip()
        score = float(line[2].strip())
        
        # Update the student's score in the dictionary
        if name in name_and_score:
            name_and_score[name] += score
        else:
            name_and_score[name] = score
        
        # Read the next line from the file
        line = data.readline().split("\t")
    
    # Close the file
    data.close()

    # Print the student scores in alphabetical order
    for name, score_sum in sorted(name_and_score.items()):
        print(name + "\t" + str(score_sum))

except FileEmpty as e:
    # Handle FileEmpty exceptions
    print(e)

except BadLine as e:
    # Handle BadLine exceptions
    print(e)

except IOError as e:
    # Handle I/O errors
    print("I/O error occurred: ", strerror(e.errno))

except Exception as e:
    # Handle any other exceptions
    print("An error occurred: ", e)