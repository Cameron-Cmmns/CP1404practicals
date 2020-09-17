"""CP1404 - Practicals - prac_05"""

COLOUR_NAMES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4",
                "AZURE1": "#f0ffff", "BEIGE": "#f5f5dc", "BISQUE": "#ffe4c4",
                "BLACK": "#000000", "BLANCHEDALMOND": "#ffebcd", "BLUE1": "#0000ff",
                "BlueViolet": "#8a2be2"}
print(COLOUR_NAMES)

colour_code = input("Enter colour name: ").upper()

while colour_code:
    if colour_code in COLOUR_NAMES:
        print(COLOUR_NAMES[colour_code])
    else:
        print("Invalid colour name")
    colour_code = input("Enter colour name: ").upper()
