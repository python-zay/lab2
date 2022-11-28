#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1a
#Convert 121,981.2298001 into a string
print(str(121981.2298001))


# In[2]:


#1b
#Convert 121,981.2298001 into an integer
print(int(121981.2298001))


# In[15]:


#1c
#Convert 121,981.2298001 to the nearest 3 decimal places
value=121981.2298001
print("the result of rounding to the nearest 3 decimal places is ",round(value,3))


# In[17]:


#1d
##are these asking the same thing??
#Convert 121,981.2298001 to the nearest thousandth
value=121981.2298001
print("the result of rounding to the nearest thousandth is ",round(value,3))


# In[70]:


#2a) Create a variable with the mentioned string as its
#value. Manage the string by using a combination of
#quotation marks and/or an escape character. apple = 'im learning "basic" python'
string = 'Im learning "basic" python'
string2 = 'I am also learning to code in java in my compsci course'
print(string)


# In[84]:


#2b)Print a message communicating the courses that you
#have taken so far in college. Be sure to use tabs and new
#lines for each item.

#2c)
##Not sure how to single out only the names of the courses
string = 'Im learning "basic" python'
string2 = 'I am also learning to code in java in my compsci course.'
string3 = 'In addition to also learning about databases in my databases course.'
print(string.upper())
print(string2.upper())
print(string3.upper())


# In[85]:


#2d)
##Not sure how to single out only the names of the courses
string = 'Im learning "basic" python'
string2 = 'I am also learning to code in java in my compsci course.'
string3 = 'In addition to also learning about databases in my databases course.'
print(string.lower())
print(string2.lower())
print(string3.lower())


# In[86]:


#2e)
##Not sure how to single out only the names of the courses
string = 'Im learning "basic" python'
string2 = 'I am also learning to code in java in my compsci course.'
string3 = 'In addition to also learning about databases in my databases course.'
print(string.title())
print(string2.title())
print(string3.title())


# In[96]:


#3a) 3b) 3c) 3d)
## cant find a way to subtract the two strings or make age and int so i can subtract the age from the year
string4 = "Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements.It's a sign that the current block will end if the indentation decreases. Thus,the program's visual structure accurately represents its semantic structure.The recommended indent size is four spaces"
print('visual' in string4)
print('Visual' in string4)
print('program' in string4)
print('accur' in string4)


# In[24]:


#4a #4b #4c #5
##cant find a way incorporate f and also have the inputs capitalize but found another way to display it 
fname = input("What is your name? ")
##ask for last name
lname =input("What is your last name? ")
##ask for age
age = input("How old are you? ")
##year you were born
year = 2022
print( 'Hello ' + fname.title() + " " + lname.title() + " " + 'are you ' + age + ' years old?' + " " + 'and were you born in ' + str(year) + ' minus your age')


# In[ ]:


#6
#the 20th term in the Fibonacci sequence is 6765
#the 100th term in the Fibonacci sequence is 354,224,848,179,261,915,075
#the 110th term in the Fibonacci sequence is 26,925,748,508,234,281,076,009
#there are 10 digits that appear in the provided photo

