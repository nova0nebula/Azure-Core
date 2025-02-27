import os
import importlib.util
import sys

# Variables
custom_modules: list = []
custom_module_commands: list = []
custom_commands_to_modules: dict = {}
system_commands: list = []  # This will now only contain functions, not names
system_command_names: list = []
system_commands_to_command_names: dict = {}

# Get the absolute path of the current working directory
current_dir: str = os.path.dirname(os.path.realpath(__file__))

# Specify the relative path to the modules folder (one level up to 'modules')
custom_modules_folder: str = os.path.join(current_dir, "../modules")
system_commands_folder: str = os.path.join(current_dir, "../core/system_commands")

# Resolve the absolute path
custom_modules_folder: str = os.path.abspath(custom_modules_folder)
system_commands_folder: str = os.path.abspath(system_commands_folder)

# Add folder to sys.path so Python can find the modules
sys.path.append(custom_modules_folder)
sys.path.append(system_commands_folder)

# Loop through all files in the folder and import .py files (custom modules)
for filename in os.listdir(custom_modules_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name: str = filename[:-3]  # Remove '.py' to get the module name
        command_name: str = filename[:-10]  # Remove '_module' to get name of command to execute the module
        file_path: str = os.path.join(custom_modules_folder, filename)

        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Assuming the function to execute is 'execute_<command_name>'
        execute_function_name = f"execute_{command_name}"
        if hasattr(module, execute_function_name):
            execute_function = getattr(module, execute_function_name)
            custom_commands_to_modules[command_name] = execute_function  # Store function instead of string
        else:
            print(f"Warning: {execute_function_name} not found in {filename}")

# Dynamically load system commands and associate them with their execution functions
for filename in os.listdir(system_commands_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        system_command_name: str = filename[:-3]  # Remove '.py' to get the system command name
        system_command: str = filename[:-11]  # Remove '_command' to get the name of the command
        file_path: str = os.path.join(system_commands_folder, filename)

        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(system_command_name, file_path)
        system = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(system)

        # Get the function from the imported module (assuming the function is named 'execute_<system_command>')
        execute_function_name = f"execute_{system_command}"
        if hasattr(system, execute_function_name):
            execute_function = getattr(system, execute_function_name)
            system_commands_to_command_names[system_command] = execute_function  # Store function instead of string
        else:
            print(f"Warning: {execute_function_name} not found in {filename}")