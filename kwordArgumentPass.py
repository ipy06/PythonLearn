"""
Keyword argument passing.

Python offers another convention for passing arguments, where the meaning of 
the argument is dictated by its name, not by its position - it's called keyword argument passing.

Don't use a non-existent parameter name!

"""
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

