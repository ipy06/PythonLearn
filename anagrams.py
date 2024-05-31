def anagrams(first_text, second_text):
    """
    This function determines if two strings are anagrams

    Args:
    first_text (str): The first string
    second_text (str): The second string

    Returns:
    bool: True if the strings are anagrams, False otherwise
    """
    first_text = first_text.replace(" ", "").lower()
    second_text = second_text.replace(" ", "").lower()
    for char in first_text:
        if char not in second_text:
            return False
    return True

first_text = input("please enter the first string: ")
second_text = input("please enter the second string: ")
if anagrams(first_text,second_text):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
