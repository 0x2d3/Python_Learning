# Comprehension ：：
o_number = []
for i in range(1, 10):
    if i % 2 == 0:
        o_number.append(i)
print(o_number)
# List Comprehension ：
'''format : [expression for item in iterable if condition]'''
o_number_1 = [i for i in range(1, 10) if i % 2 == 0]
print(o_number_1)
# Dict Comprehension：
'''format : {key_expression : value_expression for item in iterable if condition}'''
o_number_2 = {i: i * i for i in range(1, 10)}
print(o_number_2)
# Set Comprehension：
'''format : {expression for item in iterable if condition}'''
o_number_3 = {i for i in range(1, 10) if i % 2 == 0}
print(o_number_3)
# Generate Comprehension：
'''format : (expression for item in iterable if condition)'''
o_number_4 = (i for i in range(1, 10) if i % 2 == 0)
for num in o_number_4:
    print(num)

# Scope follows the LEGB rule: Local -> Enclosing -> Global -> Built-in

# Example 1: Local Scope
def my_function():
    x = 10  # Local scope
    print(x)

my_function()  # Output: 10


# Example 2: Enclosing Scope (Nested Function)
def outer_function():
    x = 20  # Enclosing scope
    def inner_function():
        print(x)  # Accessing the enclosing variable
    inner_function()

outer_function()  # Output: 20


# Example 3: Global Scope
x = 30  # Global scope

def my_function():
    print(x)  # Accessing the global variable

my_function()  # Output: 30


# Example 4: Built-in Scope
# Accessing a built-in function 'len'
print(len("hello"))  # Output: 5


# LEGB Scope Lookup:
# When you reference a variable, Python searches for it in the following order:

# 1. Local Scope (within the current function or method)
# 2. Enclosing Scope (if there are any enclosing functions)
# 3. Global Scope (top-level variables in the module)
# 4. Built-in Scope (functions and variables provided by Python, like `print`, `len`)

# Example: Scope Lookup Order
x = 100  # Global scope

def outer():
    x = 200  # Enclosing scope
    def inner():
        x = 300  # Local scope
        print(x)  # Local scope variable will be printed
    inner()

outer()  # Output: 300
# Scope Modification:
# You can modify variables in the enclosing or global scope using the `nonlocal` and `global` keywords.
# Example: Modifying Enclosing Scope
x = 100  # Global scope
def outer():
    x = 200  # Enclosing scope
    def inner():
        nonlocal x  # Refers to the enclosing scope variable
        x = 300  # Modify the enclosing scope variable
        print(x)  # Output: 300
    inner()
outer()  # Output: 300
# Example: Modifying Global Scope
x = 100  # Global scope
def outer():
    global x  # Refers to the global scope variable
    x = 200  # Modify the global scope variable
    print(x)  # Output: 200

outer()  # Output: 200

# Closure: A function that remembers the values of variables from its enclosing scope even after the enclosing scope has finished executing.
def outer(x):
    def inner(y):
        return "Hello " + x + ", " + y  # inner function remembers the value of x from outer function
    return inner
greeting = outer("Alice")
print(greeting("World"))  # Output: Hello Alice, World
# Decorators: A function that takes another function as an argument and extends its behavior without explicitly modifying it.

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
counter1 = make_counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2


# *args and **kwargs: A way to pass a variable number of arguments to a function.
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_function(1, 2, 3, a="4", b="5")  # Output: Positional arguments: (1, 2, 3) Keyword arguments: {'a': 4, 'b': 5}

web = {"google": "www.google.com", "github": "www.github.com", "stackoverflow": "www.stackoverflow.com"}
google_index = 0
for i, (key, valus) in enumerate(web.items()):
    print(f"index : {i}\n key : {key}\n value : {valus}")

# Iterator
# Define a simple iterator
class MyIterator:
    def __init__(self, data):
        self.data = data  # Store the data
        self.index = 0  # Initialize index

    def __iter__(self):
        return self  # An iterator must return itself

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration  # Stop iteration when out of bounds
        value = self.data[self.index]  # Get the current value
        self.index += 1  # Move to the next index
        return value


# Create an iterator instance
my_iter = MyIterator([1, 2, 3, 4])

# Iterate over the custom iterator
for item in my_iter:
    print(item)  # Output: 1 2 3 4

# Demonstrating iterable and iterator behavior
lst = [1, 2, 3]  # List is an iterable
iter_lst = iter(lst)  # Get an iterator from the list
print(next(iter_lst))  # Output: 1
print(next(iter_lst))  # Output: 2


# Generator function acting as an iterator
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2


# Or ：
# Generator expression to create an iterator
my_iter = (x for x in range(5))

# Iterating over the generator
print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# Using a for loop to consume the rest
for value in my_iter:
    print(value) # Aotumatic StopIteration