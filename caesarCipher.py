def cipher(text):
    """
    This is a function that implements the ceaser cipher
    where every letter of the message is replaced by its nearest consequent 
    (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.

    Args:
    text (str): The text to be encrypted.

    Returns:
    str: The encrypted text.
    """
    cipher = ''

    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

    return cipher

def decipher(text):
    """
    This is a function that implements the decryption of the ceaser cipher
    where every letter of the message is replaced by its nearest precedent
    (B becomes A, C becomes B, and so on). The only exception is A,
    which becomes Z.
    """
    decipher = ''

    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        decipher += chr(code)

    return decipher


def run():
    text_to_cipher = input("please enter the text you would like to cipher: ")
    ciphered_text = cipher(text_to_cipher)
    print("The ciphered text is: ", ciphered_text)
    text_to_decipher = input("please enter the ceaser text you would like to decipher: ")
    deciphered_text = decipher(text_to_decipher)
    print("The deciphered text is: ", deciphered_text)


run()