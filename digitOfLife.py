"""
This script calculates a person's digit of life based off of their date of birth
"""

date_of_birth = input("please enter your date of birth in the format MMDDYYYY or YYYYMMDD or YYYYDDMM:\n")

while len(date_of_birth) > 1:
    sum = 0
    for num in date_of_birth:
        if not num.isdigit():
            continue
        else:
            sum += int(num)
    date_of_birth = str(sum)

print("your digit of life is: " + str(sum))