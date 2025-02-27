import os
import stat
import time
import colorama
from colorama import Fore, Style

colorama.init()

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

def list_directory(path=".", detailed=False):
    """List directory contents, with optional detailed view"""
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
        return
    except PermissionError:
        print(f"ls: cannot access '{path}': Permission denied")
        return

    for file in files:
        full_path: str = os.path.join(path, file)
        file_stat = os.stat(full_path)

        # Get file attributes
        permissions: str = get_permissions(file_stat.st_mode)
        size: int = file_stat.st_size
        mod_time: str = time.strftime("%Y-%m-%d %H:%M", time.localtime(file_stat.st_mtime))

        # Apply color coding
        if stat.S_ISDIR(file_stat.st_mode):
            color: str = Fore.BLUE  # Directories in blue
        elif file_stat.st_mode & stat.S_IXUSR:
            color: str = Fore.GREEN  # Executable files in green
        else:
            color: str = Fore.WHITE  # Regular files in white

        if detailed:
            print(f"{permissions} {size:>8} {mod_time} {color}{file}{Style.RESET_ALL}")
        else:
            print(f"{color}{file}{Style.RESET_ALL}")

# Main System Function
def execute_ls(prompt):
    parts: list = prompt.split()
    detailed = "-l" in parts

    if len(parts) > 1 and parts[-1] != "-l":
        list_directory(parts[-1], detailed)
    else:
        list_directory(".", detailed)