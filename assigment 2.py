#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.What are the two values of the Boolean data type? How do you write them?

#A1. the 2 boolean DT are True and False and we write by:


# In[2]:


True


# In[3]:


False


# In[4]:


#2. What are the three different types of Boolean operators?
#A2. AND , OR, NOT


# In[ ]:


#3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
#values for the operator and what it evaluate ).
#A3.


X	    Y     =  X and Y
False	False =  False
True	False =  False
False	True  =  False
True	True  =  True 

X	     Y    =  X or Y
False	False =  False
True	False =  True
False	True  =  True
True	True  =  True

X	 not  X
True =  False
False = True


# In[ ]:


#4.  What are the values of the following expressions?

(5 & 4) and (3 == 5) --> False
not (5 > 4) --> False
(5 > 4) or (3 == 5) --> True
not ((5 > 4) or (3 == 5)) -->
(True and True) and (True == False) --> False
(not False) or (not True) --> True


# In[3]:


#5. What are the six comparison operators?

#A5. <= , >= , >, < , == , != 


# In[ ]:


#6. How do you tell the difference between the equal to and assignment operators?Describe a
#    condition and when you would use one.

# the main difference would be the symbols used , for equal to we use "==" and for assignment "=".
Example
num = 10
if num % 2 == 0:
    print("The number is even.")
    


# In[4]:


#7. Identify the three blocks in this code:

spam = 0
if spam == 10: # 1st
    print('eggs')
if spam > 5: #2nd
    print('bacon')
else: #3rd
    print('ham')
    print('spam')
    print('spam')


# In[6]:


#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

spam = input("enter a value: ")

if spam == "1":
    print("Hello")
elif spam == "2":
    print("Howdy")
else:
    print("Greetings!")


# In[7]:


#9.If your programme is stuck in an endless loop, what keys you’ll press?

#A9. press "ctrl + c"


# In[8]:


#10. How can you tell the difference between break and continue?

#A10. The "break" statement is used to exit a loop prematurely, typically based on a certain condition. 
#     The "continue" statement is used to skip the rest of the current iteration of a loop and proceed to the next iteration.


# In[9]:


#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

#A11. range(10) --> will give a sequence from starting 0 to 9
#     range(0, 10) --> it explicitly define the starting point(0)and end point(10) but this will also give 0-9
#     range(0,10,1) --> it explicitly defined with both a starting point (0), a stop point (10), and a step value (1)


# In[ ]:


#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#    program that prints the numbers 1 to 10 using a while loop.

#A12. 
for i in range(1,11):
    print(i)

i = 1
while i<= 10:
    print(i)
    i+=1


# In[ ]:


#13. If you had a function named bacon() inside a module named spam, how would you call it after
#    importing spam?

#A13. spam.bacon()

