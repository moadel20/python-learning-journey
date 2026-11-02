# Calculator
import math
def combining_numbers () : 
    while True : 
        try: 
            x = float(input("Enter First number: "))
            y = float(input("Enter second number: "))
            print(f"Adding = {x + y} ")
            break
        except ValueError : 
            print("Entre a true value.")

def subtraction_of_numbers () : 
    while True : 
        try: 
            x = float(input("Enter First number: "))
            y = float(input("Enter second number: "))
            print(f"Subtraction = {x - y }")
            break
        except ValueError : 
            print("Entre a true value.")

def division_of_numbers () : 
    while True : 
        try: 
            x = float(input("Enter First number: "))
            y = float(input("Enter second number: "))
            print(f"Division = {x / y}")
            break
        except ValueError : 
            print("Entre a true value.")
        except ZeroDivisionError : 
            print("You can't divide by Zero ")

def multiplying_numbers () : 
    while True : 
        try: 
            x = float(input("Enter First number: "))
            y = float(input("Enter second number: "))
            print(f"Multiplying = {x * y }")
            break
        except ValueError : 
            print("Entre a true value.")

def power_number () : 
    while True : 
        try: 
            x = float(input("Enter the base: "))
            s = int(input("Enter the exponent \: "))
            print(f"Squre root = {x ** s } ")
            break
        except ValueError : 
            print("Entre a true value.")
        except OverflowError : 
            print("the result is too large.")

def get_remainder() : 
    while True : 
        try: 
            x = float(input("Enter First number: "))
            y = float(input("Enter second number: "))
            print(f"remainder of division = {x % y } ")
            break
        except ValueError : 
            print("Entre a true value.")
        except ZeroDivisionError :
            print("You can't Division by zero.")

def floor_division() : 
    while True : 
        try: 
            x = float(input("Enter First number: "))
            y = float(input("Enter second number: "))
            print(f"Floor Divisiton = {x // y} " ) 
            break
        except ValueError : 
            print("Entre a true value.")
        except ZeroDivisionError : 
            print("You can't divide by Zero.")

def square_root () : 
    while True : 
        try: 
            x = float(input("Enter your number:"))
            

            if x < 0 :
                print("Square root of a negative number is not a real number.")
            else:
                print(f"Square Root = {math.sqrt(x)}")
                break
        except ValueError : 
            print("Entre a valid number.")
def cube_root () : 
    while True : 
        try: 
            x = float(input("Enter First number:"))
            print(f"Cube root = { math.copysign(abs(x) ** (1/3), x)} ")
            break
        except ValueError : 
            print("Entre a true value.")

print("""
    1  Adding numbers
    2  Subtracting  numbers
    3  Dividing numbers
    4  Multiplying numbers
    5  Squaring numbers
    6  Remainder of numbers division
    7  Square root
    8  Cube root
    9  Floor Division
    0  to  Exist
    """)
while True : 
    try : 
        ch = int(input("Enter what you want:"))
        match ch : 
            case 1 : 
                combining_numbers()
            case 2 :
                subtraction_of_numbers()
            case 3 : 
                division_of_numbers()
            case 4 : 
                multiplying_numbers()
            case 5 : 
                power_number()
            case 6 :
                get_remainder()
            case 7 : 
                square_root()
            case 8 :
                cube_root()
            case 9 : 
                floor_division()
            case 0 : 
                print("Good Bye")
                break
            case _:
                print("Enret corect chose.")
    except ValueError:
        print("Enter corect value.")
