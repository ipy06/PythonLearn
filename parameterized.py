"""
Mixing positional and keyword arguments

You can mix both fashions if you want - there is only one unbreakable rule: 
you have to put positional arguments before keyword arguments.


"""

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.

adding(1, 2, 3) # valid
adding(c = 1, a = 2, b = 3) # valid
adding(3, c = 1, b = 2) # valid

# adding(3 , a = 1, b = 2) # invalid because the positional assignment takes priority and assigned 3 to a
# then the keyword assignment wanted to assign 1 to a, causing a TypeError as there are multiple 
# values/assignments for a

adding(4, 3, c = 2) # valid but unnecessary for this function




def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction("James", "Doe") # prints James Doe
introduction("Henry") # prints "Hello, my name is Henry Smith"
introduction(first_name="William") # prints "Hello, my name is William Smith"

# From above we can deduce that when you initialize the formal parameter it maintains that value as
# It's default assignment in case ther isn't any.


def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction() # valid

introduction(last_name="Hopkins") # valid




