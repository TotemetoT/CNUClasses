"""
Demo handling lists
"""

starting_list = [0, 1, 2]
print("Starting list:",starting_list)
add_ten = [value + 10 for value in starting_list]
print("List comprehension + 10 (zybooks 9.8) :", add_ten)

num_names=["zero", "one", "two"]
set_names = len(num_names)*[""]  # create list of empty strings same size

print("num_names list:")
print(num_names)

print("original set_names:")
print(set_names)

print("for name in num_names:")
for name in num_names:
    print(name)

print("for index in range(len(num_names)):")
for index in range(len(num_names)):
    print(index)

print("for index, name in enumerate(num_names):")
for index, name in enumerate(num_names):
    print("{} : {} : {}".format(index, name, num_names[index]))
    set_names[index] = name # Use index in another list at least as big

print("Modified set_names:")
print(set_names)

print("Loop nesting example")
for index0, name0 in enumerate(num_names):
    for index1, name1 in enumerate(num_names):
        print("{} {} : {} {}".format(index0, index1, name0, name1))
