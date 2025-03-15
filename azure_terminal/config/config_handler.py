import json
import os

# System Library Importing
from system_library import Colour

# Define default values
DEFAULT_CONFIG = {
    "prompt_colour": "RESET",
    "error_colour": "RED",
    "error_underline": "TRUE",
    "output_colour": "RESET"
}

# Allowed values for validation
VALID_COLOURS = [
    "BLACK", "WHITE", "RED", "GREEN", "YELLOW", "BLUE", "CYAN", "MAGENTA",
    "LIGHTBLACK", "LIGHTBLUE", "LIGHTCYAN", "LIGHTGREEN",
    "LIGHTMAGENTA", "LIGHTRED", "LIGHTWHITE", "LIGHTYELLOW", "RESET"
]
VALID_BOOLEAN = ["TRUE", "FALSE"]

# Get the configuration file path
current_dir: str = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE: str = os.path.abspath(os.path.join(current_dir, "../config/appearance.json"))

# Load the existing JSON file or create an empty dictionary if file is missing
try:
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}

# Validate and update configuration
config_values = {}

for key, default_value in DEFAULT_CONFIG.items():
    # Get the current value or set it to the default
    value = data.get(key, default_value).upper()

    # Validate based on type
    if key.endswith("_colour") and value not in VALID_COLOURS:
        value = default_value  # Reset to default if invalid

    if key.endswith("_underline") and value not in VALID_BOOLEAN:
        value = default_value  # Reset to default if invalid

    # Update JSON data and store in config_values
    data[key] = value
    config_values[key] = value

# Save the validated data back to the JSON file
with open(CONFIG_FILE, "w") as file:
    json.dump(data, file, indent=2)

# Ensure colors exist in AnsiColour
config_values["prompt_colour"] = getattr(Colour, config_values["prompt_colour"], Colour.RESET)
config_values["error_colour"] = getattr(Colour, config_values["error_colour"], Colour.RED)
config_values["output_colour"] = getattr(Colour, config_values["output_colour"], Colour.RESET)

# Convert boolean values to Python boolean type
config_values["error_underline"] = config_values["error_underline"] == "TRUE"

# Assigning values to their respective variables
prompt_colour = config_values["prompt_colour"]
error_colour = config_values["error_colour"]
error_underline = config_values["error_underline"]
output_colour = config_values["output_colour"]