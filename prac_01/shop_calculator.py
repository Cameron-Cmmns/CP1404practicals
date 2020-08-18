"""
CP1404/CP5632 - Practical
Find total price of a number of items, each with different prices

"""

number_of_items = int(input("Number of items: "))
total_price = 0

for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price >= 100:
    total_price -= total_price * 0.1

print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
