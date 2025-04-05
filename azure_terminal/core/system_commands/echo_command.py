# Python Importing

# System Library Importing
from system_library import Colour

# Config Importing
from azure_terminal.config.config_handler import prompt_colour, output_colour

# System Command Execution
def execute_echo(prompt):
    parts: list = prompt.split(" ")
    if parts[-1] in ["help","-help"]:
        help_message = f"""─────────────────────────────────────
        Azure Terminal - Help
─────────────────────────────────────
Command: echo
Usage  : echo <Text>
Purpose: Displays text to the standard output.

Description:
  The 'echo' command displays text to the standard output.
  
Example:
  {prompt_colour}azure-core${Colour.RESET} echo Hello, World!
  {output_colour}Hello, World!{Colour.RESET}

Notes:
  - If no arguments are given, a newline will be outputted..

─────────────────────────────────────"""
        print(help_message)
        return
    else:
        del parts[0]
        if len(parts) > 1:
            for i in parts:
                print(f"{output_colour}{i}{Colour.RESET}")
        elif len(parts) == 0:
            print()
        else:
            print(f"{output_colour}{parts[-1]}{Colour.RESET}")