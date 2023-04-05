

# As a user, I want to be able to see the menu in a formatted way so that I can order my meal.

appetiser = ["hummus", "sliders", "salad"]
mains = ["beef burger", "chicken steak", "seafood pasta"]
dessert = ["date cake", "vanilla sponge", "mango sorbet"]

message = "Hello, welcome. What would you like to order?"
print(message)

print("appetiser")
print(appetiser)
print("mains")
print(mains)
print("dessert")
print(dessert)


# As a user, I want to be able to order three seperate times and have my responses added to a list so they are not forgotton

appetiser_order = input("What would you like for appetiser?")

mains_order = input("What would you like to order for a main?")

dessert_order = input("What can I get you for dessert?")

# As a user, I want to have my order read back to me in a formatted way so I know what I ordered

food_ordered = [appetiser_order, mains_order, dessert_order]
print("So you have ordered...")
print(food_ordered)
