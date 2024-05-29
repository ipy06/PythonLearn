def mysplit(string, sep=' '):
    """
    This is a function implementing my version of the string's split method

    Args:
    string (str): The string to be split
    separator (str): The separator to split the string by (default is space)

    Returns:
    list: A list of strings split by the separator
    """
    separator = sep  # default separator is a space
    string_list = []
    sub_string = ""

    for char in string:
        if char == separator:
            if sub_string != "":
                string_list.append(sub_string)
                sub_string = ""
        else:
            sub_string += char
    if separator not in sub_string and sub_string != "":
        string_list.append(sub_string)
    return string_list


# TESTS
print(mysplit("Hello World"))   # Output: ['Hello', 'World']
print(mysplit("To be or not to be, that is the question"))  # Output: ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
print(mysplit("To be or not to be,that is the question"))   # Output: ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
print(mysplit("   "))   # Output: []
print(mysplit(" abc ")) # Output: ['abd']
print(mysplit(""))  # Output: []

