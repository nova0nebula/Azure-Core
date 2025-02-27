# Importing
from azure_terminal.core.modules_importing import custom_module_commands, custom_modules, custom_commands_to_modules, system_commands, system_commands_to_command_names, system_command_name

# Executing commands
def execute_command(prompt: str):
    # Check if prompt matches system commands
    if prompt in system_commands_to_command_names:
        execute_system_function = system_commands_to_command_names[prompt]
        execute_system_function(prompt)  # Call the corresponding system function
    # Check if prompt matches custom module commands
    elif prompt in custom_commands_to_modules:
        execute_module_function = custom_commands_to_modules[prompt]
        execute_module_function(prompt)  # Call the corresponding module function
    else:
        print(f"Unknown command: {prompt}")