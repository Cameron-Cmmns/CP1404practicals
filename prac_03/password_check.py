"""
CP1401 - Prac_03
Password Check
"""


def main():
    password_input = input("Enter a password: ")

    if check_password_length(password_input):
        display_password(password_input)
    else:
        print("The password is too short")


def check_password_length(user_input):
    if len(user_input) >= 3:
        return True
    else:
        return False


def display_password(password_input):
    password_length = len(password_input)

    for x in range(0, password_length):
        print("*", end="")


main()
