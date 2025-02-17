# Importing
import os
import time
import random
import sys
import math
import colorama
from colorama import Fore, Style, Back
import platform
import subprocess
import shutil
import getpass
import datetime
import socket
import traceback
import requests
import inspect
import string
from difflib import get_close_matches

# Variables
azure_core_commands = {
    "Restart-System": "Restarts the system",
    "Shutdown-System": "Shutdowns the system",
    "help": "Show this help menu",
    "version": "Display the current version of Azure Core",
    "--version": "Display the current version of Azure Core",
    "clear": "Clears the screen",
    "list-modules": "Lists all the modules",
    "changelog": "Displays the changelog",
    "checkupdates": "Checks for updates",
    "ls": "List files in the current directory",
    "sysinfo": "Display system information",
    "tasklist": "Show running processes",
    "ipconfig": "Show network configuration"
}
prefix_colours = {"ac": Fore.CYAN, "sq": Fore.YELLOW, "-p": Fore.MAGENTA}
prefixes = {"ac": "Azure Core", "sq": "Subject Quizzer", "-p": "Prefix"}
dash = "-" * os.get_terminal_size().columns
username = getpass.getuser()
cwd = os.getcwd()
system_name = platform.system()
uname = platform.uname()
GITHUB_VERSION_FILE = "https://raw.githubusercontent.com/nova0nebula/Azure-Core/main/Azure_Core_Dependencies/Azure_Core_Version.txt"
GITHUB_URL = "https://github.com/nova0nebula/Azure-Core.git"
VERSION_FILE = "Azure_Core_Dependencies/Azure_Core_Version.txt"
CHANGELOG_FILE = "Azure_Core_Dependencies/Azure_Core_Changelog.txt"

# Ascii Art
azure_command_ascii = '''
                ╔═╗┌─┐┬ ┬┬─┐┌─┐  ╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐
                ╠═╣┌─┘│ │├┬┘├┤   ║  │ │││││││├─┤│││ ││
                ╩ ╩└─┘└─┘┴└─└─┘  ╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘
'''


# Function - clear_screen()
def clear_screen():
  try:
    if sys.stdout.isatty():  # Check if running in a terminal
      if platform.system() == "Windows":
        os.system("cls")  # Standard Windows command
      else:
        os.system("clear")  # Standard Unix/Linux/macOS command
    else:
      print("\033c", end="")  # ANSI escape sequence (works in most terminals)
  except Exception as e:
    print(f"{Fore.RED}Unexpected error: {e}{Fore.RESET}")


# Function - parse_version_data(data)
def parse_version_data(data):
  version_info = {}
  for line in data.splitlines():
    if " =~-$=-~= " in line:
      key, value = line.split(" =~-$=-~= ")
      version_info[key.strip()] = value.strip()
  return version_info


# Function - get_github_files()
def get_github_files():
  repo_url = "https://api.github.com/repos/nova0nebula/Azure-Core/contents"
  response = requests.get(repo_url)
  if response.status_code == 200:
    return response.json()
  else:
    print("Error fetching GitHub repository files.")
    return []


# Function - check_for_updates(prompt, debug_mode)
def check_for_updates(prompt, debug_mode):
  debug_mode = str(debug_mode).lower()
  try:
    response = requests.get(GITHUB_VERSION_FILE)
    if response.status_code == 200:
      latest_version = parse_version_data(response.text)
    else:
      print("Failed to fetch latest version.")
      return
    if os.path.exists(VERSION_FILE):
      with open(VERSION_FILE, "r") as file:
        local_version = parse_version_data(file.read())
    else:
      print("Local version file not found. Running update...")
      return
    latest_version_number = latest_version.get("Version", "").strip()
    local_version_number = local_version.get("Version", "").strip()
    if debug_mode == "true":
      print(
          f"{Fore.RED}DEBUG - Local Version: '{latest_version_number}'{Fore.RESET}"
      )
      print(
          f"{Fore.RED}DEBUG - Latest Version: '{local_version_number}'{Fore.RESET}"
      )
    if latest_version_number != local_version_number:
      print(f"{Fore.RED}\033[1;4mUpdate Available!\033[0m{Fore.RESET}")
      print(f"Current Version: {Fore.RED}{local_version_number}{Fore.RESET}")
      print(
          f"Current Build: {Fore.RED}{local_version.get('Build', 'Unknown')}{Fore.RESET}"
      )
      print(
          f"Release Date: {Fore.RED}{local_version.get('Released', 'Unknown')}{Fore.RESET}\n"
      )
      print(
          f"New Version: {Fore.LIGHTGREEN_EX}{latest_version_number}{Fore.RESET}"
      )
      print(
          f"New Build: {Fore.LIGHTGREEN_EX}{latest_version.get('Build', 'Unknown')}{Fore.RESET}"
      )
      print(
          f"Release Date: {Fore.LIGHTGREEN_EX}{latest_version.get('Released', 'Unknown')}{Fore.RESET}"
      )
      print("Download the latest version from GitHub!")
    else:
      print(
          f"{Fore.LIGHTGREEN_EX}You are using the latest version!{Fore.RESET}")
  except Exception as e:
    print(f"{Fore.RED}Unexpected error: {e}{Fore.RESET}")


# Function - print_invalid_prefix(prefix)
def print_invalid_prefix(prefix):
  """ Handles incorrect prefixes """
  print(
      f"{Fore.RED}Error: '{prefix}' is not a recognized system. Use '\033[4m-p help\033[0m{Fore.RED}' for prefix help.{Fore.RESET}"
  )


# Function - get_azure_version()
def get_azure_version():
  """ Displays Azure Core version, system info, and Python version """
  version = ""
  build_info = ""
  release_date = ""
  if os.path.exists(VERSION_FILE):
    with open(VERSION_FILE, "r") as file:
      for line in file:
        line = line.strip()
        if line.startswith("Version"):
          version = "Azure Core " + line.split(" =~-$=-~= ")[1]
        elif line.startswith("Build"):
          build_info = "Build " + line.split(" =~-$=-~= ")[1]
        elif line.startswith("Released"):
          release_date = line.split(" =~-$=-~= ")[1]
  else:
    version = "Azure Core v1.0.0"
    build_info = "Build 1000 (Stable)"
    release_date = "February 2025"

  print(f"{Fore.CYAN}{version}{Fore.RESET}")
  print(f"{Fore.GREEN}{build_info}{Fore.RESET}")
  print(f"{Fore.MAGENTA}Released on: {release_date}{Fore.RESET}")


# Function - get_azure_core_changelog(prompt)
def get_azure_core_changelog(prompt):
  try:
    print(dash)
    with open(CHANGELOG_FILE, "r") as file:
      changelog = file.read()
      print(changelog)
    print(dash)
  except PermissionError:
    print_permission_error(prompt)
  except FileNotFoundError:
    print_file_error(prompt)
  except Exception as e:
    print(f"{Fore.RED}Unexpected error: {e}{Fore.RESET}")


# Function - azure_core_help_screen(prompt)
def azure_core_help_screen(prompt):
  print("\033[1;4mAzure Core Help Screen\033[0m\nAvailable Commands:\n")
  for command, usage in azure_core_commands.items():
    length = 22 - len(command)
    print(f"{Fore.CYAN}ac{Fore.RESET} {command}" + (" " * length) +
          f"{Fore.GREEN}- {usage}{Fore.RESET}")


# Function - print_error(command)
def print_error(command):
  """ Prints a PowerShell-style error message with suggestions """
  try:
    raise OSError(
        f"\n{Fore.RED}Azure Core : The term '{command}' is not recognized as a command.{Fore.RESET}"
    )
  except OSError as e:
    tb = traceback.extract_tb(e.__traceback__)
    filename, lineno, funcname, text = tb[-1]
    error_line = lineno
    error_char = len(command)
    print(
        f"\n{Fore.RED}Azure Core : The term '{command}' is not recognized as a command.{Fore.RESET}"
    )
    print(f"At line:{error_line} char:{error_char}")
    print(f"+ {command}")
    print(f"  {Fore.RED}~{'~' * len(command)}{Fore.RESET}")
    print(
        f"    {Fore.YELLOW}CategoryInfo{Fore.RESET}          : ObjectNotFound: ({command}:String) []"
    )
    print(
        f"    {Fore.YELLOW}FullyQualifiedErrorId{Fore.RESET} : CommandNotFoundException"
    )

  matches = get_close_matches(command, azure_core_commands, n=1, cutoff=0.6)
  if matches:
    print(f"\n{Fore.CYAN}Did you mean: {matches[0]}?{Fore.RESET}\n")
  else:
    print("\n")


# Function - print_permission_error(prompt)
def print_permission_error(command):
  """ Prints a PowerShell-style permission error """
  try:
    raise PermissionError(
        f"\n{Fore.RED}Azure Core : Access denied. You do not have permission to run '{command}'.{Fore.RESET}"
    )
  except PermissionError as e:
    tb = traceback.extract_tb(e.__traceback__)
    filename, lineno, funcname, text = tb[-1]
    error_line = lineno
    error_char = len(command)
  print(
      f"\n{Fore.RED}Azure Core : Access denied. You do not have permission to run '{command}'.{Fore.RESET}"
  )
  print(f"At line:{error_line} char:{error_char}")
  print(f"+ {command}")
  print(f"    {Fore.RED}~{'~' * len(command)}{Fore.RESET}")
  print(
      f"    {Fore.YELLOW}CategoryInfo{Fore.RESET}          : PermissionDenied: ({command}:String) []"
  )
  print(
      f"    {Fore.YELLOW}FullyQualifiedErrorId{Fore.RESET} : PermissionError\n"
  )


# Function - print_file_error(command)
def print_file_error(command):
  """ Prints a PowerShell-style file error """
  try:
    raise FileNotFoundError(
        f"\n{Fore.RED}Azure Core : The system cannot find the file specified: '{command}'.{Fore.RESET}"
    )
  except FileNotFoundError as e:
    tb = traceback.extract_tb(e.__traceback__)
    filename, lineno, funcname, text = tb[-1]
    error_line = lineno
    error_char = len(command)
  print(
      f"\n{Fore.RED}Azure Core : The system cannot find the file specified: '{command}'.{Fore.RESET}"
  )
  print(f"At line:{error_line} char:{error_char}")
  print(f"+ {command}")
  print(f"    {Fore.RED}~{'~' * len(command)}{Fore.RESET}")
  print(
      f"    {Fore.YELLOW}CategoryInfo{Fore.RESET}          : FileNotFound: ({command}:String) []"
  )
  print(
      f"    {Fore.YELLOW}FullyQualifiedErrorId{Fore.RESET} : FileNotFoundError\n"
  )


# Function - handle_azure_core_commands(actions, prompt)
def handle_azure_core_commands(action, prompt):
  if action in azure_core_commands:
    try:
      if action in ["version", "--version"]:
        get_azure_version()
      elif action == "Restart-Computer":
        azure_core_main()
      elif action == "Shutdown-Computer":
        print(f"{Fore.GREEN}Exiting Azure Core...{Fore.RESET}")
        sys.exit()
      elif action == "clear":
        azure_core_main()
      elif action == "help":
        azure_core_help_screen(prompt)
      elif action == "list-modules":
        print("Module not yet implemented.")
      elif action == "sysinfo":
        print(f"{Fore.WHITE}\033[1;4mSystem Information\033[0m{Fore.RESET}")
        print(f"{Fore.CYAN}Username: {username}{Fore.RESET}")
        print(f"{Fore.GREEN}Cwd: {cwd}{Fore.RESET}")
        print(
            f"{Fore.MAGENTA}Platform: {system_name} {platform.release()}{Fore.RESET}"
        )
        print(f"{Fore.YELLOW}System: {uname.system}{Fore.RESET}")
        print(f"{Fore.RED}Node: {uname.node}{Fore.RESET}")
        print(f"{Fore.GREEN}Release: {uname.release}{Fore.RESET}")
        print(f"{Fore.BLUE}Version: {uname.version}{Fore.RESET}")
        print(f"{Fore.LIGHTBLACK_EX}Machine: {uname.machine}{Fore.RESET}")
        print(f"{Fore.LIGHTBLUE_EX}Processor: {uname.processor}{Fore.RESET}")
      elif action == "changelog":
        get_azure_core_changelog(prompt)
      elif action == "checkupdates":
        check_for_updates(prompt, "false")
      elif action == "ls":
        for file in os.listdir('.'):
          print(file)
      elif action == "tasklist":
        if platform.system() == "Windows":
          os.system("tasklist")
        else:
          os.system("ps aux")
      elif action == "ipconfig":
        if platform.system() == "Windows":
          os.system("ipconfig")
        else:
          os.system("ifconfig" if os.system("ifconfig") == 0 else "ip a")
    except PermissionError:
      print_permission_error(prompt)
    except FileNotFoundError:
      print_file_error(prompt)
    except Exception as e:
      print(f"{Fore.RED}Unexpected error: {e}{Fore.RESET}")
  else:
    print_error(prompt)


# Main Function - azure_core_main()
def azure_core_main():
  clear_screen()
  print("\033[1;4mAzure Core\033[0m")
  print("Copyright (C) Azure Command. All rights reserved.\n")
  while True:
    prompt = str(
        input(
            f"{Fore.CYAN}AC{Fore.RESET} C:\\{Fore.LIGHTYELLOW_EX}Users{Fore.RESET}\\{username}> "
        ))
    parts = prompt.split()
    if not parts:
      continue
    prefix = parts[0].lower()
    action = " ".join(parts[1:])
    if prefix in prefixes:
      if prefix == "ac":
        handle_azure_core_commands(action, prompt)
      elif prefix == "sq":
        print(
            f"{Fore.YELLOW}Subject Quizzer system is not implemented yet!{Fore.WHITE}"
        )
      elif prefix == "-p":
        if action == "help":
          print("\033[1;4mPrefix Help Menu\033[0m")
          for key, value in prefixes.items():
            colour = prefix_colours.get(key, Fore.RESET)
            length = 25 - len(key)
            print(f"{colour}{key}" + (" " * length) +
                  f"{colour}- {value}{Fore.RESET}")
    else:
      print_invalid_prefix(prefix)


# Calling main function
azure_core_main()
