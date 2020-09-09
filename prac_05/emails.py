"""CP1404 - Practicals - prac_05
   Emails
"""

# email_dict = {}
#
# user_input = input("Enter Email: ")
#
# name = ""
# user_email = ""
#
#
# emails = user_input.split()
# where_to_cut = user_input.find("@")
#
# while user_input != "":
#
#     for email in emails:
#         user_email = email
#         name = email_dict.get(email, user_input[0:where_to_cut])
#         email_dict[email] = name
#
#         check_is_name = input("Is your name {}? (Y/n) ".format(name))
#         check_is_name.lower()
#         if check_is_name == "y":
#             email_dict[email] = name
#         elif check_is_name == "n":
#             new_name = input("Name: ")
#             email_dict[email] = new_name
#         else:
#             print("Invalid input")
#
#     user_input = input("Enter Email: ")
#
# for name in emails:
#     print("{} ({})".format(email_dict[name], user_email))


def main():
    email_to_name = {}

    email = input("Email: ")
    is_valid = True

    while email != "":

        name = get_name_from_email(email)

        confirmation = input("Is this your name {}? (Y/n)".format(name)).lower()

        # This if looks a little bad, but I am unsure how to put it in a function.
        # previous tries stopped the entire program from working.

        if confirmation == "n" or confirmation == "no":
            name = input("Name: ")

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
