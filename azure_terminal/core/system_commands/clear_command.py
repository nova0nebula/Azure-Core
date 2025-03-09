import os

def execute_clear(prompt):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')