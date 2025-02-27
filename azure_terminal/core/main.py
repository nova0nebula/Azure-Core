# Importing
from azure_terminal.core.command_handling import execute_command

# Main Function
def azure_terminal_main():
    while True:
        prompt: str = str(input("azure-core$ ")).strip()
        execute_command(prompt)

# Calling main function
if __name__ == "__main__":
    azure_terminal_main()