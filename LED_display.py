def led_display(string_of_num):
    """
    This function takes in a string of integers and output it in LED form.
    The function works as a seven-display device

    Args:
    string_of_num (int) - This is the input of a string of intgers

    Returns:
    None

    """
    # Initialize the display
    display = {
        '0': ['###','# #','# #','# #','###'],
        '1': ['  #','  #','  #','  #','  #'],
        '2': ['###','  #','###','#  ','###'],
        '3': ['###','  #','###','  #','###'],
        '4': ['# #','# #','###','  #','  #'],
        '5': ['###','#  ','###','  #','###'],
        '6': ['###','#  ','###','# #','###'],
        '7': ['###','  #','  #','  #','  #'],
        '8': ['###','# #','###','# #','###'],
        '9': ['###','# #','###','  #','###']
    }

    string_of_num = str(string_of_num)
    list_of_disp = []
    string = ""

    for i in range(5):
        for char in string_of_num:
            if char.isnumeric():
                string += display[char][i]
                string += " "
        list_of_disp.append(string)
        string = ""

    for elem in list_of_disp:
        print(elem)


print("Welcome to the LED display program\nUse the command Ctrl + C to exit the program for Windows and Linux\nUse the command + c for macOS\n")
while True:
    try:
        num = int(input("Enter a number you wish to display in LED form: "))
        led_display(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    except KeyboardInterrupt:
        print("\n\nExiting program.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
