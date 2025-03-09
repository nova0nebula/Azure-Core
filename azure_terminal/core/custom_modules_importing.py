import os
import importlib.util
import sys

# Variables
custom_modules: list = []
custom_module_commands: list = []
custom_module_command_to_function_name: dict = {}

# Get the absolute path of the current working directory
current_dir: str = os.path.dirname(os.path.realpath(__file__))

# Specify the relative path to the modules folder (one level up to 'modules')
custom_modules_folder: str = os.path.join(current_dir, "../modules")

# Resolve the absolute path
custom_modules_folder: str = os.path.abspath(custom_modules_folder)

# Add folder to sys.path so Python can find the modules
sys.path.append(custom_modules_folder)

# Dynamically load custom module commands and associate them with their execution functions
for filename in os.listdir(custom_modules_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        custom_module_file_name: str = filename[:-3]  # Remove '.py' to get the custom module file name
        custom_module_command: str = filename[:-10]  # Remove '_module.py' to get name of command
        file_path: str = os.path.join(custom_modules_folder, filename)

        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(custom_module_file_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Assuming the function to execute is 'execute_<command_name>'
        execute_function_name = f"execute_{custom_module_command}"
        if hasattr(module, execute_function_name):
            execute_function = getattr(module, execute_function_name)
            custom_module_command_to_function_name[custom_module_command] = execute_function  # Store function instead of string
        else:
            print(f"Warning: {execute_function_name} not found in {filename}")