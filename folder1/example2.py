import os

def insecure_password():
    password = "123456"  # Issue: hardcoded_password_string
    return password

def command_injection(user_input):
    command = "echo " + user_input  # Issue: subprocess_without_shell_equals_true
    os.system(command)

# Example usage
password = insecure_password()
user_input = input("Enter your input: ")
command_injection(user_input)
