# System Library Importing
from system_library import Format, Colour

# Local Importing
from azure_terminal.core.system_modules_importing import system_command_to_function_name
from azure_terminal.core.custom_modules_importing import custom_module_command_to_function_name
from azure_terminal.config.config_handler import error_colour, error_underline

# Executing commands
def execute_command(prompt: str):
    parts: list = prompt.split(" ")
    command_name: str = parts[0]
    # Check if prompt matches system commands
    if command_name in system_command_to_function_name:
        execute_system_function = system_command_to_function_name[command_name]
        execute_system_function(prompt)  # Call the corresponding system function
    # Check if prompt matches custom module commands
    elif command_name in custom_module_command_to_function_name:
        execute_custom_module_function = custom_module_command_to_function_name[command_name]
        execute_custom_module_function(prompt)  # Call the corresponding custom module function
    else:
        print(f"{error_colour}Unknown command: {Format.underline(prompt) if error_underline else prompt}{Colour.RESET}")