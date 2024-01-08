# Script for the copilot_test program

def get_name():
    # Function to get user input
    return input("Enter your name: ")

def greet(name):
    # Function to print a greeting message
    print("Hello, " + name + "!")

def main():
    # Main function orchestrating program flow
    name = get_name()
    greet(name)