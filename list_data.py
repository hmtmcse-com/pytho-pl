# List Data Type
list_data = ["Name", 23, True, 23.2]

# Print List
print(list_data)

# Access List Element & Print, We have to use Index for access value, the index start with 0
element = list_data[1]
print(element)

# Negative Indexing
# Negative indexing means start from the end
element = list_data[-2]
print(element)

# Range of Indexes
# We can specify a range of indexes by specifying where to start and where to end the range.
element = list_data[0:3]
print(element)

# Without specifying first index of Range
# Automatically take the first index 0
element = list_data[:3]
print(element)

# Without specifying last index of Range
# Automatically take the last index length of the list
element = list_data[2:]
print(element)

# Check element exist on List
if "Name" in list_data:
    print("Yes the key is exist")

# Print each Element from the List
for element in list_data:
    print(element)

# Update List Element
list_data[0] = "My Name"
print(list_data)

# Update List Element by Range
list_data[0:2] = ["What is your Name", 100]
print(list_data)


# Append Element into List
list_data.append("New Element")
print(list_data)

# Insert Element into List
list_data.insert(1, "Insert Element")
print(list_data)


# Extend List
# The elements will be added to the end of the list.
other_list_data = ["db", "program", "math"]
list_data.extend(other_list_data)
print(list_data)

list_data[0] = "Name"

# Remove Element from the List by value
list_data.remove("Name")
print(list_data)

# Remove Specified Index from the List
list_data.pop(1)
print(list_data)

# If we do not specify the index, the pop() method removes the last item.
list_data.pop()
print(list_data)

# The del keyword also removes the specified index
del list_data[0]
print(list_data)
