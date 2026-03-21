# Add Two Numbers
a = 15
b = 12
res = a+b
print(res)

# Using user input
a = input("First number: ")
b = input("Second number: ")

# converting input to float and adding
res = float(a) + float(b)
print(res)

# Using Function
def add(a,b):
    return a+b

# initializing numbers
a = 10
b = 5

# calling functions
res = add(a,b)

print(res)

# Minimum of two numbers in Python
a = 7
b = 3
print(min(a, b))

# Using Conditional Statements
a = 5
b = 7

if a < b:
    print(a)
else:
    print(b)

# Using Conditional Statements through user input
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

if a < b:
    print(a, "is the minimum number")
print(b, "is the minimum number")
