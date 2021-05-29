# Key is String
string_dictionary = {
    "name": "Touhid Mia",
    "country": "Bangladesh",
    "age": 28,
}

# Key is Number
number_dictionary = {
    1: "Name",
    2: "Country",
    3.5: "Age",
}

# Key is Tuple
tuple_dictionary = {
    ("name", 1, "age"): "This is Tuple key's value",
}

# Python Dictionary Manipulation
manipulate_dictionary = {
    "name": "Touhid Mia",
    "country": "Bangladesh",
    "age": 28,
}

# Print Dictionary
print(manipulate_dictionary)


# Check key exist on dictionary
if 'name' in manipulate_dictionary:
    print("Yes key exist")
else:
    print("No key not exist")

# Get Element from Dictionary & print
element = manipulate_dictionary['name']
print(element)
# Or
element = manipulate_dictionary.get('name')
print(element)


# Get Length of a Dictionary & print
count = len(manipulate_dictionary)
print(count)


# Get Keys from Dictionary & print
keys = manipulate_dictionary.keys()
print(keys)

# Get Values from Dictionary & print
values = manipulate_dictionary.values()
print(values)

# Print each Element from the Dictionary
for key in manipulate_dictionary:
    print("Key : " + key)
    value = manipulate_dictionary[key]
    print("Value : " + str(value))

# Or
for key, value in manipulate_dictionary.items():
    print("Key : " + key)
    print("Value : " + str(value))


# Update Dictionary value by key & print
manipulate_dictionary["name"] = "Mia Bhai"
print(manipulate_dictionary)
# Or
manipulate_dictionary.update({"name": "Mia Bhai Updated with new Way"})
print(manipulate_dictionary)


# Add Element into Dictionary & print
manipulate_dictionary["address"] = "Rangpur"
print(manipulate_dictionary)
# Or
manipulate_dictionary.update({"address": "Rangpur, Bangladesh"})
print(manipulate_dictionary)


# Remove Element from Dictionary
del manipulate_dictionary["name"]
print(manipulate_dictionary)
# Or
manipulate_dictionary.pop("age")
print(manipulate_dictionary)

# Remove the last Element from Dictionary
manipulate_dictionary.popitem()
print(manipulate_dictionary)
