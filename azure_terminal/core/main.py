# System Library Importing
from system_library import Colour

# Local Importing
from azure_terminal.core.command_handling import execute_command
from azure_terminal.config.config_handler import prompt_colour

# Main Function
def azure_terminal_main():
    while True:
        prompt: str = str(input(f"{prompt_colour}azure-core$ {Colour.RESET}")).strip()
        execute_command(prompt)

# Calling main function
if __name__ == "__main__":
    azure_terminal_main()