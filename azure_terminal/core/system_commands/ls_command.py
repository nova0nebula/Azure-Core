# Python Importing
import os
import stat
import time

# System Library Importing
from system_library import Colour, Style

# Config Importing
from azure_terminal.config.config_handler import prompt_colour, output_colour

# Function to convert file mode to ls-style string (e.g., '-rw-r--r--')
def get_permissions(mode):
    """Convert file mode to ls-style string (e.g., '-rw-r--r--')"""
    is_dir = "d" if stat.S_ISDIR(mode) else "-"
    perms = [
        "r" if mode & stat.S_IRUSR else "-",
        "w" if mode & stat.S_IWUSR else "-",
        "x" if mode & stat.S_IXUSR else "-",
        "r" if mode & stat.S_IRGRP else "-",
        "w" if mode & stat.S_IWGRP else "-",
        "x" if mode & stat.S_IXGRP else "-",
        "r" if mode & stat.S_IROTH else "-",
        "w" if mode & stat.S_IWOTH else "-",
        "x" if mode & stat.S_IXOTH else "-",
    ]
    return is_dir + "".join(perms)

# Function to convert file size to human-readable format (e.g., KB, MB)
def human_readable_size(size):
    """Convert file size to human-readable format (e.g., KB, MB)"""
    units = ["B", "KB", "MB", "GB", "TB"]
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.1f}{units[index]}"

# Function to list directory contents with various options
def list_directory(path=".", show_hidden=False, detailed=False, human_readable=False):
    """List directory contents with optional detailed view, hidden files, and human-readable sizes"""
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
        return
    except PermissionError:
        print(f"ls: cannot access '{path}': Permission denied")
        return

    # Display files with options applied
    for file in files:
        # Skip hidden files unless '-a' is specified
        if not show_hidden and file.startswith("."):
            continue

        full_path = os.path.join(path, file)
        file_stat = os.stat(full_path)

        # Get file attributes
        permissions = get_permissions(file_stat.st_mode)
        size = human_readable_size(file_stat.st_size) if human_readable else file_stat.st_size
        mod_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(file_stat.st_mtime))

        # Apply color coding based on file type
        if stat.S_ISDIR(file_stat.st_mode):
            color = Colour.BLUE  # Directories in blue
        elif file_stat.st_mode & stat.S_IXUSR:
            color = Colour.GREEN  # Executable files in green
        else:
            color = Colour.WHITE  # Regular files in white

        # Print file information
        if detailed:
            print(f"{permissions} {size:>8} {mod_time} {color}{file}{Style.RESET_ALL}")
        else:
            print(f"{color}{file}{Style.RESET_ALL}")

# Function to display the help message for 'ls' command
def display_help():
    """Display help message for the 'ls' command"""
    help_message = f"""─────────────────────────────────────
        Azure Terminal - Help
─────────────────────────────────────
Command: ls
Usage  : ls <Option>
Purpose: Lists files and directories in the current directory.

Description:
  The 'ls' command displays a list of files and directories.
  By default, it shows basic file names without additional details.

Options:
  -a  : Show all files, including hidden ones.
  -l  : Display detailed file information.
  -h  : Show file sizes in human-readable format.
  
Example:
  {prompt_colour}azure-core${Colour.RESET} ls -l
  {output_colour}-rw-r--r-- 1 user group  1234 Jan 01 12:00 file.txt{Colour.RESET}

Notes:
  - Multiple options can be combined (e.g., 'ls -lah').
  - Hidden files start with a '.' and are not shown unless '-a' is used.

─────────────────────────────────────"""
    print(help_message)

# System Command Execution
def execute_ls(prompt):
    """Parse and execute 'ls' command with options"""
    parts = prompt.split(" ")

    # Extract options (those starting with '-')
    options = [part for part in parts if part.startswith("-")]

    # Determine the path (last part is path if it doesn't start with '-')
    path = parts[-1] if len(parts) > 1 and not parts[-1].startswith("-") else "."

    # Parse flags for options
    show_hidden = "a" in "".join(options)
    detailed = "l" in "".join(options)
    human_readable = "h" in "".join(options)

    # Display help message if requested
    if "help" in parts or "-help" in parts:
        display_help()
        return
    else:
        # Execute the ls command with the provided options
        if path == "." or os.path.isdir(path):
            list_directory(path, show_hidden, detailed, human_readable)
        else:
            print(f"ls: cannot access '{path}': No such file or directory")
            return