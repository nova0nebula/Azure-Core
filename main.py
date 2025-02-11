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
import inspect
import string
from difflib import get_close_matches

# Variables
commands = ["Restart-Computer", "help", "Shutdown-Computer"]
dash = "-" * 70
username = getpass.getuser()
cwd = os.getcwd()
system_name = platform.system()

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


# Main Function - azure_command_main()
def azure_command_main():
  clear_screen()
  print("\033[1;4mAzure Core\033[0m")
  print("Copyright (C) Azure Command. All rights reserved.\n")
  while True:
    prompt = str(
        input(f"AC C:\\{Fore.LIGHTYELLOW_EX}Users{Fore.WHITE}\\{username}> ")
    ).strip()
    parts = prompt.split()
    cmd = parts[0] if parts else ""

    if cmd in commands:
      try:
        if cmd == "Restart-Computer":
          azure_command_main()
      except PermissionError:
        print_permission_error(prompt)
      except FileNotFoundError:
        print_file_error(prompt)
      except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Fore.RESET}")
    elif cmd.lower() == "exit":
      print(f"{Fore.GREEN}Exiting Azure Command...{Fore.RESET}")
      break
    else:
      print_error(prompt)


# Calling main function
azure_command_main()
