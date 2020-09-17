from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 200)

age_guitar = gibson.get_age()
age_another_guitar = another.get_age()

print("{} get_age() - Expected 98. Got {}".format(gibson.name, age_guitar))
print("{} get_age() - Expected 7. Got {}".format(another.name, age_another_guitar))


print(gibson)
