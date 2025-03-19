# Python Importing
import os
import importlib.util
import sys

# Variables
system_command_to_function_name:dict = {}
custom_module_command_to_function_name: dict = {}

# Get the absolute path of the current working directory
current_dir: str = os.path.dirname(os.path.realpath(__file__))

# Define system commands and custom modules folder paths
folders: dict = {
    "system": os.path.abspath(os.path.join(current_dir, "../core/system_commands")),
    "custom": os.path.abspath(os.path.join(current_dir, "../modules"))
}

# Add folders to sys.path so Python can find the modules
for folder in folders.values():
    sys.path.append(folder)

# Function to dynamically load modules and associate commands with execute functions
def load_commands(folder: str, suffix: str, command_dict: dict):
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename != "__init__.py":
            command_name: str = filename[:-len(suffix)]     # Extract command name by removing suffix
            file_path: str = os.path.join(folder, filename)
            
            # Dynamically import the module
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find and store the execute function
            execute_function_name: str = f"execute_{command_name}"
            if hasattr(module, execute_function_name):
                command_dict[command_name] = getattr(module, execute_function_name)
            else:
                print(f"Warning: {execute_function_name} not found in {filename}")

# Load system commands and custom modules
load_commands(folders["system"], "_command.py", system_command_to_function_name)
load_commands(folders["custom"], "_module.py", custom_module_command_to_function_name)