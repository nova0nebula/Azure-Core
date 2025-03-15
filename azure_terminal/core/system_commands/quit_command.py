# System Library Importing
from system_library import Colour

# Config Importing
from azure_terminal.config.config_handler import prompt_colour, output_colour

# System Command Execution
def execute_quit(prompt):
    parts: list = prompt.split(" ")
    if parts[-1] in ["help","-help"]:
        help_message = f"""─────────────────────────────────────
        Azure Terminal - Help
─────────────────────────────────────
Command: quit
Usage  : quit
Purpose: Exits the Azure Terminal safely.

Description:
  The 'quit' command allows you to exit the terminal session.
  It ensures all processes are closed properly before exiting.
  
Example:
  {prompt_colour}azure-core${Colour.RESET} quit
  {output_colour}Exiting Azure Terminal...{Colour.RESET}

Notes:
  - There are no additional arguments required.
  - If you have unsaved work, make sure to save it before quitting.

─────────────────────────────────────"""
        print(help_message)
        return
    else:
        print(f"{output_colour}Quitting...{Colour.RESET}")
        exit()