def cipher(text, shift=0):
    """
    This is a function that implements an improved ceaser cipher
    where every letter of the message is replaced by its supplied consequent 
    (A becomes B ... B, B becomes C ... C, and so on).

    Args:
    text (str): The text to be encrypted.
    shift (int): The number of positions each letter in the plaintext should be shifted down the alphabet

    Returns:
    str: The encrypted text.
    """
    cipher = ''

    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        if char.isupper():
            code = ord(char) + shift
            if code > ord('Z'):
                code = ord('A') + (shift - (ord('Z') - ord(char)) - 1)
            cipher += chr(code)
        else:
            code = ord(char) + shift
            if code > ord('z'):
                code = ord('a') + (shift - (ord('z') - ord(char)) - 1)
            cipher += chr(code)

    return cipher

def decipher(text, shift=0):
    """
    This is a function that implements the decryption of the improved ceaser cipher
    where every letter of the message is replaced by its specified precedent
    (B becomes A ... Z, C becomes B ... A, and so on depending on the shift specified).

    Args:
    text (str): The text to be decrypted.
    shift (int): The number of positions each letter in the plaintext should be shifted up the alphabet

    Returns:
    str: The decrypted text.
    """
    decipher = ''

    for char in text:
        if not char.isalpha():
            decipher += char
            continue
        if char.isupper():
            code = ord(char) - shift
            if code < ord('A'):
                code = ord('Z') - (shift - (ord(char) - ord('A')) - 1)
            decipher += chr(code)
        else:
            code = ord(char) - shift
            if code < ord('a'):
                code = ord('z') - (shift - (ord(char) - ord('a')) - 1)
            decipher += chr(code)
    
    return decipher


def run():
    text_to_cipher = input("please enter the text you would like to cipher: ")
    shift = 0

    while True:
        try:
            shift = int(input("enter the amount of points you want to shift the cipher: (1 - 25): "))
            if shift < 1 or shift > 25:
                raise ValueError
            break
        except ValueError:
            print("You have entered and invalid shift, please try again!")
        except KeyboardInterrupt:
            print("Exiting Program.")
        except:
            print("An error has occurred, please try again.")
            
    ciphered_text = cipher(text_to_cipher, shift)
    print("The ciphered text is: ", ciphered_text)


    text_to_decipher = input("please enter the ceaser text you would like to decipher: ")
    while True:
        try:
            shift = int(input("enter shift point of the original cipher (1 - 25): "))
            if shift < 1 or shift > 25:
                raise ValueError
            break
        except ValueError:
            print("You have entered and invalid shift, please try again!")
        except KeyboardInterrupt:
            print("Exiting Program.")
        except:
            print("An error has occurred, please try again.")

    deciphered_text = decipher(text_to_decipher, shift)
    print("The deciphered text is: ", deciphered_text)


run()