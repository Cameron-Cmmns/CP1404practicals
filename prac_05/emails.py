"""CP1404 - Practicals - prac_05
   Emails
"""

def main():
    email_to_name = {}

    email = input("Email: ")
    is_valid = True

    while email != "":

        name = get_name_from_email(email)

        confirmation = input("Is this your name {}? (Y/n)".format(name)).lower()

        # This if looks a little bad, but I am unsure how to put it in a function.
        # previous tries stopped the entire program from working.
        if confirmation == "y":
            pass
        elif confirmation == "n":
            name = input("Name: ")
        else:
            print("Invalid input")
            is_valid = False
            while not is_valid:
                confirmation = input("Is this your name {}? (Y/n)".format(name)).lower()

                if confirmation == "y":
                    is_valid = True
                    pass
                elif confirmation == "n":
                    name = input("Name: ")
                    is_valid = True
                else:
                    print("Invalid input")
                    is_valid = False

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
