# System Library Importing
from system_library import Colour

# Config Importing
from azure_terminal.config.config_handler import prompt_colour, output_colour

# Custom Module Execution
def execute_math(prompt):
    # Remove 'math ' prefix from the prompt
    prompt_with_no_math: str = prompt.removeprefix("math ")

    # Split the prompt into parts (should separate by space, but can be customized for more complex expressions)
    parts: list = prompt_with_no_math.split(" ")
    parts_length: int = len(parts)
    
    if parts[-1] in ["help","-help"]:
        help_message = f"""─────────────────────────────────────
        Azure Terminal - Help
─────────────────────────────────────
Command: math
Usage  : math <operand1> <operator> <operand2> <precision>
Purpose: Performs mathematical operations using two operands.

Description:
  The 'math' command performs a basic arithmetic operation between two operands.
  It supports addition (+), subtraction (-), multiplication (*), division (/), and modulo (%).
  You can specify the precision for the result, or use '-' for no rounding.

Example:
  {prompt_colour}azure-core${Colour.RESET} math 10 + 5 2
  {output_colour}Result: 10 + 5 2 = 15.0{Colour.RESET}

Notes:
  - The operands can be any numbers (positive or negative).
  - Supported operators are +, -, *, /, and %.
  - The precision can be a positive integer or '-' for no rounding.
  - If dividing, make sure the second operand is not zero.
  - If no precision is given, the result will be shown as a float with full precision.

─────────────────────────────────────"""
        print(help_message)
        return
    elif parts_length < 4:  # Check if we have a valid input with enough parts for an operation
        print("Error: Invalid math operation. Format should be 'math <operand1> <operator> <operand2> <precision>'")
        return

    operand1: float = float(parts[0])  # First operand
    operator: str = str(parts[1])         # Operator
    operand2: float = float(parts[2])  # Second operand
    precision: str = str(parts[3])

    # Perform the operation based on the operator
    if operator == "+":
        result: float = operand1 + operand2
    elif operator == "-":
        result: float = operand1 - operand2
    elif operator == "*":
        result: float = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result: float = operand1 / operand2
    elif operator == "%":
        result: float = operand1 % operand2
    else:
        print("Error: Invalid operator. Supported operators are +, -, *, /, %")
        return
    
    # Round off to precision
    if precision == "-":
        pass
    else:
        precision: int = int(precision)
        result: float = round(result, precision)

    # Output the result
    print(f"{output_colour}Result: {operand1} {operator} {operand2} {precision} = {result}{Colour.RESET}")
