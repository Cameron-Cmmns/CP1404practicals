"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    marking = return_score(score)
    print(marking)



def return_score(score):
    if score <= 50 and score >= 0:
        return "Bad"
    elif score > 50 and score < 90:
        return "Passable"
    elif score >= 90 and score <= 100:
        return "Excellent"
    else:
        return "Invalid Score"


main()
