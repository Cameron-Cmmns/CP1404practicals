"""
CP1404 - Practicals - Week 6: Classes
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection:
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} typing, Reflection = {}, first appeared in {}".format(self.name, self.typing,
                                                                             self.reflection, self.year)
