def is_palindrome(text):
    """
    This is a function that determines if a string of text is a palindrome

    Args:
    text (str): The string of text to check

    Returns:
    bool: True if the text is a palindrome, False otherwise
    """
    text = text.lower().replace(" ","")
    text = "".join(char for char in text if char.isalnum())
    return text == text[::-1]

# Tests
print(is_palindrome("Ten animals I slam in a net"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Eleven animals I slam in a net"))