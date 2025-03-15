# Python Importing
import random

# Local Importing
from azure_terminal.modules.math_module import execute_math

def random_operator_generator():
    number: int = random.randint(0,4)
    if number == 0:
        return "+"
    elif number == 1:
        return "-"
    elif number == 2:
        return "*"
    elif number == 3:
        return "/"
    elif number == 4:
        return "%"

def math_module_tests():
    while True:
        times_to_run: str = str(input("Enter how many times to run test - "))
        maximum_number: int = int(input("Enter the maximum number for random number generator - "))
        rounding_off: str = str(input("Enter a number to round off too, input '-' for no rounding - "))
        if times_to_run.isdigit():
            for i in range(0,int(times_to_run)):
                prompt: str = f"math {random.randint((maximum_number*-1),maximum_number)} {random_operator_generator()} {random.randint((maximum_number*-1),maximum_number)} {rounding_off}"
                execute_math(prompt)
            exit()
        else:
            print("Please enter a digit number.")

if __name__ == "__main__":
    math_module_tests()