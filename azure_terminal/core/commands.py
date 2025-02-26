import os
import importlib.util
import sys

# Variables
modules: list = []
module_commands: list = []

# Get the absolute path of the current working directory
current_dir: str = os.path.dirname(os.path.realpath(__file__))

# Specify the relative path to the modules folder (one level up to 'modules')
modules_folder: str = os.path.join(current_dir, "../modules")

# Resolve the absolute path
modules_folder: str = os.path.abspath(modules_folder)

# Add folder to sys.path so Python can find the modules
sys.path.append(modules_folder)

# Loop through all files in the folder and import .py files
for filename in os.listdir(modules_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name: str = filename[:-3]  # Remove '.py' to get the module name
        command_name: str = module_name[:-7] # Remove '_module' to get name of command to execute the module
        modules.append(module_name)
        module_commands.append(command_name)
        file_path: str = os.path.join(modules_folder, filename)

        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)