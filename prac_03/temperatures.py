"""
CP1404/CP5632 - Practical
Temperature Conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
CELSIUS = 0
FAHRENHEIT = 0


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            fahrenheit_to_celcuis()
        elif choice == "F":
           celsius_to_fahrenheit()
        else:
            print("Invalid option")
        print(MENU)

        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    # fahrenheit = celsius * 9 / 5 + 32
    print("Result: {:.2f} C".format(celsius))


def fahrenheit_to_celcuis():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


main()
