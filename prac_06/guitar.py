"""
CP1404 - Practicals - Week 6
Classes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2020 - self.year
        return age

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def is_vintage(self):
        if self.year >= 50:
            return True
        else:
            return False
