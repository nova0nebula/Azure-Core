import os
import importlib.util
import sys

# Variables
system_commands: list = []
system_command_names: list = []
system_command_to_function_name: dict = {}

# Get the absolute path of the current working directory
current_dir: str = os.path.dirname(os.path.realpath(__file__))

# Specify the relative path to the modules folder (one level up to 'modules')
system_commands_folder: str = os.path.join(current_dir, "../core/system_commands")

# Resolve the absolute path
system_commands_folder: str = os.path.abspath(system_commands_folder)

# Add folder to sys.path so Python can find the modules
sys.path.append(system_commands_folder)

# Dynamically load system commands and associate them with their execution functions
for filename in os.listdir(system_commands_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        system_file_name: str = filename[:-3]  # Remove '.py' to get the system file name
        system_command: str = filename[:-11]  # Remove '_command.py' to get the name of the command
        file_path: str = os.path.join(system_commands_folder, filename)

        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(system_file_name, file_path)
        system = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(system)

        # Get the function from the imported module (assuming the function is named 'execute_<system_command>')
        execute_function_name = f"execute_{system_command}"
        if hasattr(system, execute_function_name):
            execute_function = getattr(system, execute_function_name)
            system_command_to_function_name[system_command] = execute_function  # Store function instead of string
        else:
            print(f"Warning: {execute_function_name} not found in {filename}")