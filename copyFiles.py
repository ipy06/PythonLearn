"""
Copies the contents of a source file to a destination file.

This script prompts the user to enter the source and destination file names.
It then attempts to open the source file in binary read mode and the destination file in binary write mode.
If any errors occur during the file operations, it prints an error message and exits with the corresponding error code.

The script uses a buffer of size 65536 to read and write data in chunks, ensuring efficient file copying.
It keeps track of the total bytes written to the destination file and prints this information upon completion.

Parameters:
    None

Returns:
    None

Raises:
    IOError: If an error occurs while reading from the source file or writing to the destination file.
    Exception: If an exception occurs while creating the destination file.

Example:
    $ python file_copy.py
    Enter the source file name: source.txt
    Enter the destination file name: destination.txt
    12345 byte(s) successfully written
"""

from os import strerror  # Import the strerror function from the os module to get error messages

srcname = input("Enter the source file name: ")  # Prompt user to enter the source file name

try:
    src = open(srcname, 'rb')  # Attempt to open the source file in binary read mode
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))  # If an IOError occurs, print the error message
    exit(e.errno)  # Exit the program with the error code

dstname = input("Enter the destination file name: ")  # Prompt user to enter the destination file name

try:
    dst = open(dstname, 'wb')  # Attempt to open the destination file in binary write mode
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))  # If an exception occurs, print the error message
    src.close()  # Close the source file
    exit(e.errno)  # Exit the program with the error code

buffer = bytearray(65536)  # Create a bytearray buffer of size 65536
total = 0  # Initialize a variable to keep track of the total bytes written

try:
    readin = src.readinto(buffer)  # Read data from the source file into the buffer
    while readin > 0:  # Continue reading until there's no more data
        written = dst.write(buffer[:readin])  # Write the data from the buffer to the destination file
        total += written  # Increment the total bytes written
        readin = src.readinto(buffer)  # Read the next chunk of data
except IOError as e:
    print("Error reading or writing: ", strerror(e.errno))  # If an IOError occurs, print the error message
    exit(e.errno)  # Exit the program with the error code

print(total, 'byte(s) successfully written')  # Print the total bytes written
src.close()  # Close the source file
dst.close()  # Close the destination file