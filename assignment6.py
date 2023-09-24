#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q.1. What are keywords in python? Using the keyword library, print all the python keywords.

A1. keywords in python are reserve words which have special meaning. 
    It is immutable 
    eg. None, for etc.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'python')
A2. > must start with a letter or _
    > A variable name cannot start with a number.
    > A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    > Variable names are case-sensitive


# In[ ]:


Q.3. What are the standards and conventions followed for the nomenclature of variables in
get_ipython().run_line_magic('pinfo', 'maintainability')

A3. > Choose meaningful and descriptive names that indicate the purpose or content of the variable.
    > Use lowercase letters and separate words with underscores (_) to create variable names 
    > Do not use Python's reserved words (e.g., if, while, for, import, class) as variable names, as it can lead to confusion and errors
    > When defining constants, use all uppercase letters with underscores to separate words
    > Use CamelCase (also known as PascalCase) for class names, where each word begins with an uppercase letter (e.g., MyClass, EmployeeDetails).
    > When naming functions or methods, use a verb-noun pairing that describes the action and object 
    


# In[ ]:


get_ipython().run_line_magic('pinfo', 'name')
A4. If you use a Python keyword as a variable name, you will encounter a syntax error.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'used')
A5. In Python, the def keyword is used to define a function. A function is a 
    reusable block of code that performs a specific task or set of tasks when called.


# In[ ]:


Q.6. What is the operation of this special character ‘\’?
A6. The backslash can be used to continue a statement onto the next line when the code is too long to fit comfortably on one line


# In[ ]:


Q.7. Give an example of the following conditions:
(i) Homogeneous list
    my_list = [1,"alice",["a","b"]]
    
(ii) Heterogeneous set
    heterogeneous_set = {1, "apple", 3.14, (1, 2, 3), True}
    
(iii) Homogeneous tuple
      homogeneous_tuple = (10, 20, 30, 40, 50)


# In[ ]:


Q.8. Explain the mutable and immutable data types with proper explanation & examples.
A8. In Python, data types can be categorized as either mutable or immutable based on whether their values can be changed after they are created. Understanding the difference between mutable and immutable data types is important because it has implications for how you can manipulate and work with these types.

****Immutable Data Types:****

Immutable data types are those whose values cannot be modified after they are created. When you perform operations that appear to modify an immutable object, you are actually creating a new object with the updated value. Immutable data types in Python include:

int: Integer objects are immutable. When you perform operations like addition or subtraction on integers, you create new integer objects.


x = 5
y = x + 3  # y is a new integer with the value 8
float: Floating-point numbers are also immutable.


pi = 3.14159
str: Strings are immutable. When you concatenate or modify a string, you create a new string object.


message = "Hello"
new_message = message + ", World!"  # new_message is a new string
tuple: Tuples are immutable. You cannot change their elements once they are defined.


point = (3, 4)

****Mutable Data Types:****

Mutable data types, on the other hand, are those whose values can be modified after creation. When you modify a mutable object, you are changing the original object in place. Mutable data types in Python include:

list: Lists are mutable. You can add, remove, or modify elements within a list.


numbers = [1, 2, 3]
numbers.append(4)  # Modifies the original list
dict: Dictionaries are mutable collections of key-value pairs. You can add, remove, or modify key-value pairs.


person = {"name": "Alice", "age": 30}
person["age"] = 31  # Modifies the original dictionary
set: Sets are mutable collections of unique elements. You can add or remove elements from a set.


colors = {"red", "green", "blue"}
colors.add("yellow")  # Modifies the original set
bytearray: Bytearrays are mutable sequences of bytes. You can modify the individual bytes within a bytearray.


data = bytearray(b"Hello")
data[0] = 72  # Modifies the first byte to represent 'H'
custom objects: You can create your own custom classes with mutable attributes.

    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 25)
person.age = 26  # Modifies the age attribute of the Person object


# In[7]:


# Q.9. Write a code to create the given structure using only for loop.

i = 5
for x in range(1, i+1):
    for j in range(1, 2 * x):
        print('*', end ='')
    print()


# In[8]:


#Q.10. Write a code to create the given structure using while loop.
#A10. 
n = 5  

while n > 0:
    for i in range(n):
        print('|', end='')
    print()  
    n -= 1

