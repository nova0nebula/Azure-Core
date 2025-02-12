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
commands = ["Restart-Computer", "help", "Shutdown-Computer","version","--version","clear","list-modules"]
dash = "-" * 70
username = getpass.getuser()
cwd = os.getcwd()
system_name = platform.system()
VERSION_FILE = "Azure_Core_Dependencies/Azure_Core_Version.txt"

# Ascii Art
azure_command_ascii = '''
                ╔═╗┌─┐┬ ┬┬─┐┌─┐  ╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐
                ╠═╣┌─┘│ │├┬┘├┤   ║  │ │││││││├─┤│││ ││
                ╩ ╩└─┘└─┘┴└─└─┘  ╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘
'''


# Function - clear_screen()
def clear_screen():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def print_invalid_prefix(prefix):
  """ Handles incorrect prefixes """
  print(f"{Fore.RED}Error: '{prefix}' is not a recognized system. Use 'ac' for Azure Core commands.{Fore.RESET}")

def get_azure_version():
  """ Displays Azure Core version, system info, and Python version """
  if os.path.exists(VERSION_FILE):
      with open(VERSION_FILE, "r") as f:
          azure_core_version =  f.read().strip()
  else:
    azure_core_version = "Azure Core v1.0.0\nBuild "
  build_info = "Build 1024 (Stable)"
  release_date = "February 2025"

  print(f"\n{Fore.YELLOW}Azure Core Information:{Fore.RESET}")
  print(f"{Fore.CYAN}{azure_core_version}{Fore.RESET}")
  print(f"{Fore.GREEN}{build_info}{Fore.RESET}")
  print(f"{Fore.MAGENTA}Released on: {release_date}{Fore.RESET}")

  # Show OS and Python version
  print(f"\n{Fore.YELLOW}System Information:{Fore.RESET}")
  print(f"{Fore.CYAN}OS: {platform.system()} {platform.release()}{Fore.RESET}")
  print(f"{Fore.GREEN}Python Version: {sys.version.split()[0]}{Fore.RESET}")


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

  matches = get_close_matches(command, commands, n=1, cutoff=0.6)
  if matches:
    print(f"\n{Fore.CYAN}Did you mean: {matches[0]}?{Fore.RESET}\n")
  else:
    print("\n")


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


def print_file_error(command):
  """ Prints a PowerShell-style file error """
  print(
      f"\n{Fore.RED}Azure Core : The system cannot find the file specified: '{command}'.{Fore.RESET}"
  )
  print(f"At line:1 char:1")
  print(f"+ {command}")
  print(f"    {Fore.RED}~{'~' * len(command)}{Fore.RESET}")
  print(
      f"    {Fore.YELLOW}CategoryInfo{Fore.RESET}          : FileNotFound: ({command}:String) []"
  )
  print(
      f"    {Fore.YELLOW}FullyQualifiedErrorId{Fore.RESET} : FileNotFoundError\n"
  )

def handle_azure_core_commands(action,prompt):
  if action in commands:
    try:
      if action in ["version","--version"]:
        get_azure_version()
      elif action == "Restart-Computer":
        azure_core_main()
      elif action == "Shutdown-Computer":
        print(f"{Fore.GREEN}Exiting Azure Command...{Fore.WHITE}")
        sys.exit()
      elif action == "clear":
        azure_core_main()
      elif action == "help":
        print("Module not yet implemented.")
      elif action == "list-modules":
        print("Module not yet implemented.")
    except PermissionError:
      print_permission_error(prompt)
    except FileNotFoundError:
      print_file_error(prompt)
    except Exception as e:
      print(f"{Fore.RED}Unexpected error: {e}{Fore.WHITE}")
  else:
    print_error(prompt)

# Main Function - azure_command_main()
def azure_core_main():
  clear_screen()
  print("\033[1;4mAzure Core\033[0m")
  print("Copyright (C) Azure Command. All rights reserved.\n")
  while True:
    prompt = str(input(f"AC C:\\{Fore.LIGHTYELLOW_EX}Users{Fore.WHITE}\\{username}> "))
    parts = prompt.split()
    if not parts:
      continue
    prefix = parts[0].lower()
    action = " ".join(parts[1:])
    if prefix == "ac":
      handle_azure_core_commands(action,prompt)
    elif prefix == "sq":
      print(f"{Fore.YELLOW}Subject Quizzer system is not implemented yet!{Fore.WHITE}")
    else:
      print_invalid_prefix(prefix)


# Calling main function
azure_core_main()
