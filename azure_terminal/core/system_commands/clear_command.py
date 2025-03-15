# Python Importing
import os

# System Library Importing
from system_library import Colour

# Config Importing
from azure_terminal.config.config_handler import prompt_colour, output_colour

# System Command Execution
def execute_clear(prompt):
    parts: list = prompt.split(" ")
    if parts[-1] in ["help","-help"]:
        help_message = f"""─────────────────────────────────────
        Azure Terminal - Help
─────────────────────────────────────
Command: clear
Usage  : clear
Purpose: Clears the terminal screen.

Description:
  The 'clear' command clears the terminal screen, providing a clean workspace
  for new commands and output. It does not delete any data; it simply removes
  previous content from the terminal display.

Example:
  {prompt_colour}azure-core${Colour.RESET} clear
  {output_colour}[Terminal screen is cleared]{Colour.RESET}

Notes:
  - No arguments are required for this command.
  - If you have important information displayed, ensure it is saved before clearing.

─────────────────────────────────────"""
        print(help_message)
        return
    else:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')