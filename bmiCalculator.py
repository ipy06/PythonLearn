import os
import time

"""

This is an interactive program to calculate the BMI (Body Mass Index)

"""

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

def main():
    
    os.system("clear")
    time.sleep(2)

    print("""
        Hello and welcome to the BMI calculator!
        You can select between imperical and metric units.

        You will be asked if you want to use imperical units.
        If you select yes, you will advance to the imperical calculator
        but if you select no you will advance to the metric calculator.

        Enjoy!""")

    ans = input("\n\tWould you like to use Imperical units (yes/no) ? ").lower()
    
    if ans == "no":
        
        os.system("clear")
        print("\n\tYou have now entered the metric units calculation.\n")
        height = float(input("\tPlease Enter your height in meters(m): "))
        weight = float(input("\tPlease Enter your weight in kilograms(kg): "))
        
        return bmi(weight = weight, height = height)

    elif ans == "yes":
        
        os.system("clear")
        print("\n\tYou have selected the imperical units calculator.\n")
        weight = float(input("\tPlease enter your weight in pounds(lbs): "))
        height = input("""
        Please enter your height in feet and inches
        Example if you are 6 feet tall, enter 6,0 and
        5 feet 4 inches -> 5,4

        Please enter height here: """)
        feet, inches = int(height[0]), int(height[-1])
        weight = lb_to_kg(weight);
        height = ft_and_inch_to_m(feet, inches)
        return bmi(weight = weight, height = height)

    else:

        print("\nYou have entered an invalid input and will be redirected to the main menu.")
        time.sleep(5)
        return main()

        


print("\n\tYour BMI is:", main(), "\n\n\tBye!!!")
time.sleep(3)
