### to clear the screen in command line practice
import os
os.system('clear')

### >>> means output
###List
#list is mutable data type where is Tuples and String is immutable dataType
#Variables do not store list values directly; they store references to lists.
spam = ['cat', 'bat', 'rat', 'elephant'] #this is the main list every other example is relative with this list
spamWithInnerArray = [['cat', 'bat'], [10, 20, 30, 40, 50]]
###accessing list
spam[1] >>> 'bat'
spamWithInnerArray[0][1] >>> 'bat'
###negetive index
spam[-1] >>> 'elephant'
###getting sublists with slices
spam[0:4] >>>['cat', 'bat', 'rat', 'elephant']
spam[1:3] >>>['bat', 'rat']
spam[0:-1] >>>['cat', 'bat', 'rat']
###length of list
len(spam) >>> 4
### changing values in a list 
spam[1] = 'aardvark';
spam >>> ['cat', 'aardvark', 'rat', 'elephant'] 
spam[2] = spam[1]
spam >>> ['cat', 'aardvark', 'aardvark', 'elephant'] 
###list Concate & replication
[1, 2, 3] + ['A', 'B', 'C']
>>> [1, 2, 3, 'A', 'B', 'C']
['X', 'Y'] * 3 
>>> ['X', 'Y','X', 'Y','X', 'Y']
spam = spam + [1, 2]
spam >>> ['cat', 'bat', 'rat', 'elephant', 1, 2] 
###removing values from lists with del (You need to know index)
del spam[2]
spam >> ['cat', 'bat', 'elephant']

###loop 
for i in range(4): #for i in [0, 1, 2,, 3] same thing
    print (i)
>>> 0
    1
    2
    3

###loop through List
for singleSpam in spam :
    print(singleSpam)
>>> cat
    bat
    rat
    elephant
### loop through List using range technique
for i in range(len(spam)) :
    print ('Index ' + str(i) + ' in spam is : ' + spam[i])
>>>> Index 0 in spam is: cat
     Index 1 in spam is: bat
     Index 2 in spam is: rat
     Index 3 in spam is: elephant

### the in and not operators
'cat' in spam
>>> True
'mouse' in spam
>>> False
'cat' not in spam
>>> False
'mouse' no in spam
>>> True

###The Multiple Assignment Trick
cat = ['fat', 'orange', ,'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# you could type this line of code
size, color, disposition = cat
#warning :The Number of variables and the length of the list must be exactly equal, or Python will give you a ValueError

### Finding value in list
spam.index('cat')
>>>0
spam = ['cat', 'bat', 'rat', 'elephant', 'cat'] 
spam.index('cat') #for duplicate value index of first appearance will be return
>>>0
### adding value to lists with append() and insert()
spam.append('moose') #append value end of the list
spam
>>> ['cat', 'bat', 'rat', 'elephant', 'moose'] 
spam.insert(1, 'chicken') #first arg is index 2nd arg is newValue 
spam
>>> ['cat', 'chicken', 'bat', 'rat', 'elephant', 'moose'] 

### removing value from the list with remove();
spam.remove('bat') #you can delete by del keyword(which in stated above) if you know index or by getting index by index function 
spam
>>> ['cat', 'rat', 'elephant'] 

### sorting the values in a list with the sort() method
spam = [5, 4, 7, 2, 6]
spam.sort() #sort usages ASCIIbetical order
spam 
>> [2, 4, 5, 6, 7]
spam.sort(reverse=True)
spam 
>> [7, 6, 5, 4, 2]
spam = ['alice', 'bob', 1, 3, 2] #it can't be sort because alpha neumeric mixed
spam.sort();
spam
>>> Traceback Error : ...
spam = ['a', 'z', 'A', 'Z']
spam.sort();
spam 
>>>['A', 'Z', 'a', 'z']
spam.sort(key=str.lower)
spam
>>>['a', 'A', 'z', 'Z']

###Tuples
eggs = ('hello', 42, 0.5)
eggs[1] = 99 #you can't modified Tuples object
>>> Traceback Error
eggs = ('hello',) # If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses. Otherwise, Python will think you’ve just typed a value inside regular parentheses. The comma is what lets Python know this is a tuple value

###type checking whether its Tuples or not 
type((hello,)) #with trailing comma
>>> <class 'tuple'>
type((hello))
>>> <class 'str'>
###converting types with lists() and tuple() functions
tuple(['cat', 'bat', 'rat', 'elephant'])
>>>('cat', 'bat', 'rat', 'elephant')
list('hello')
>>>['h', 'e', 'l', 'l', 'o']
###copy a variable always holds references
spam = [0, 1, 2]
cheese = spam
cheese[1] = 'hello'
spam
>>> [0, 'hello', 2 ]
## when copy a varibale it holds its references. If you dont want this references the copy module's copy() and deepCopy() function will be needed
import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)
cheese[1] = 42
spam
>>> ['A', 'B', 'C']
cheese
>>> ['A', 42, 'C']

###### TEST
int(int('3' * 2) // 11)
>>>int( 33 // 11)
>>> 3

