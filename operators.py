# Arithmetic operators
print("---------------------------------------------------------------")
print("Arithmetic operators")
print("---------------------------------------------------------------")
a = 10
b = 11
result = a + b
print(result)


a = 12
b = 11
result = a - b
print(result)

a = 12
b = 11
result = a * b
print(result)

a = 12
b = 11
result = a / b
print(result)

a = 12
b = 11
result = a % b
print(result)

a = 2
b = 3
result = a ** b
print(result)  # same as 2*2*2

a = 9
b = 2
result = a // b
print(result)

# Comparison operators
print("---------------------------------------------------------------")
print("Comparison operators")
print("---------------------------------------------------------------")
a = 12
b = 11
result = a == b
print(result)

a = 12
b = 11
result = a != b
print(result)

a = 12
b = 11
result = a > b
print(result)

a = 12
b = 11
result = a < b
print(result)

a = 12
b = 11
result = a >= b
print(result)

a = 12
b = 11
result = a <= b
print(result)

# Logical operators
print("---------------------------------------------------------------")
print("Logical operators")
print("---------------------------------------------------------------")
a = 12
result = a < 5 and a < 10
print(result)

a = 12
result = a < 5 or a < 10
print(result)

a = 12
result = not(a < 5 or a < 10)
print(result)


# Identity operators
print("---------------------------------------------------------------")
print("Identity operators")
print("---------------------------------------------------------------")
a = 12
b = 13
result = a is b
print(result)

a = 12
b = 13
result = a is not b
print(result)


# Membership operators
print("---------------------------------------------------------------")
print("Membership operators")
print("---------------------------------------------------------------")
dictionary = {"name": "Touhid", "sex": "Male"}
result = "name" in dictionary
print(result)

dictionary = {"name": "Touhid", "sex": "Male"}
result = "name" not in dictionary
print(result)