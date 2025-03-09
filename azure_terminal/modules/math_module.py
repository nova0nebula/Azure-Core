# Main Function for mathematical operations
def execute_math(prompt):
    # Remove 'math ' prefix from the prompt
    prompt_with_no_math: str = prompt.removeprefix("math ")

    # Split the prompt into parts (should separate by space, but can be customized for more complex expressions)
    parts: list = prompt_with_no_math.split(" ")
    parts_length: int = len(parts)

    # Check if we have a valid input with enough parts for an operation
    if parts_length < 4:
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
    print(f"Result: {operand1} {operator} {operand2} = {result}")
