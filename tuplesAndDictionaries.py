"""
This is a program program to evaluate students' average scores
the program will ask for the student's name, followed by her/his single score
the names may be entered in any order
entering an empty name finishes the inputting of the data 
note : entering an empty score will raise the ValueError exception
a list of all names, together with the evaluated average score, will then be printed. 

"""


school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
