# Collections

# Lists

# array = list
#Collections
# List
# A single data types ideal
example_list = (1, True, "string")

print(example_list[0])
print(example_list[1])
print(example_list[2])
print(example_list[-1])

# First list = shopping list
# [] = list
shopping_list = ["milk", "bread", "eggs", "chocolate", "jam"]

print(shopping_list)
print(type(shopping_list))

# Accessing a particular part of the list
print(shopping_list[2])

# change an element in a list
shopping_list[2] = "butter"
print(shopping_list)
print(shopping_list[2])

# Using list methods

# adding to a list with append()
shopping_list. append("fish")
print(shopping_list)

# removing items with remove()
shopping_list. remove("bread")
print(shopping_list)

# removing the last item from a list, without specifying what it is
shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)

# Can I have a list with a mixed data types?
mixture = [1, 2, 3, 4.5, "five", "six"]
print(mixture)

# Slicing
print(mixture[1:3])

# Reverse the order of the slice
print(mixture[-3::])

# Step over
print(mixture[::2])

# Tuples

# Tuples are IMMUTABLE - it cannot be changed

tuple_example = ("bread", "eggs", "milk")
print(tuple_example)

# Dictionaries

# Another way to manage data, but they are a little more dynamic and complex

# Key-Value pairs

# Key = reference to the object
# Value = the data mechanism you wish to store the data in (e.g string, int, list, another dictionary

student_1 = {
    "name": "luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "setup"]
}

# Acess the dictionary

print(student_1["stream"])

# Access a part of the list in the dictionary
print(student_1["completed_lesson_names"][2])

# Changine a value in a dictionary
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# Changing an element of a list within a dictionary
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())

# Sets and Frozen sets

# set in python is a list that has no order/indexing

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
print(car_parts)

car_parts.add("windows")
print(car_parts)
# When windows gets added, it doesn't go in the end but rather a random place

car_parts.discard("doors")
print(car_parts)

# Frozen sets - an immutable set - won't let you change them

x = frozenset([1, 2, 3, 4])
