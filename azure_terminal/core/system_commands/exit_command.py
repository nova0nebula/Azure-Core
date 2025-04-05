# System Library Importing
from system_library import Colour

# Config Importing
from azure_terminal.config.config_handler import prompt_colour, output_colour

# System Command Execution
def execute_exit(prompt):
    parts: list = prompt.split(" ")
    if parts[-1] in ["help","-help"]:
        help_message = f"""─────────────────────────────────────
        Azure Terminal - Help
─────────────────────────────────────
Command: exit
Usage  : exit
Purpose: Exits the Azure Terminal safely.

Description:
  The 'exit' command allows you to exit the terminal session.
  It ensures all processes are closed properly before exiting.
  
Example:
  {prompt_colour}azure-core${Colour.RESET} exit
  {output_colour}Exiting Azure Terminal...{Colour.RESET}

Notes:
  - There are no additional arguments required.
  - If you have unsaved work, make sure to save it before exiting.

─────────────────────────────────────"""
        print(help_message)
        return
    else:
        print(f"{output_colour}Exiting Azure Terminal...{Colour.RESET}")
        exit()