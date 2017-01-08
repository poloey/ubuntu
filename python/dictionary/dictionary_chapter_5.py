###spam is main dictionary. all example will be relative to the spam
###dictionary is mutable datatype 
### >>> for outpur of the data
spam = {'name': 'Zophie', 'age': 7}

### keys(), values(), items()
### dict_keys, dict_values, dict_items
for v in spam.values():
for v in spam.keys():
for v in spam.items():
for k, v in spam.items():
    print ('key: ' + k + ' value: ' + str(v))
spam.keys() >>> dict_keys(['name', 'age'])
spam.values() >>> dict_values(['Zopie', 7])
spam.items() >>> dict_items([('name', 'Zopie'), ('age', 7)])
list(spam.keys()) >>> ['name', 'age']
name in spam.keys() >>> True

### get() method
#get() takes 2 arguments. 1. the key of the value to retrieve and a fallback value to return.

picnicItems = {'apple' : 5, 'cups' : 2}
print('I have ' str(picnicItems.get('apple', 0)) + ' apple')
>>> I have 5 apple
print('I have ' str(picnicItems.get('orange', 0)) + ' orange')
>>> I have 0 orange
    
###  setdefault() 
## it takes 2 arguments. first argument check wheter the key is exists or not and if not exists second argument will assign as value
spam.setdefault('color', 'black')
spam >>> {'name': 'Zophie', 'age': 7, 'color' : 'black'}
spam.setdefault('name', 'simon') #name won't change because name already preset there
spam >>> {'name': 'Zophie', 'age': 7, 'color' : 'black'}

### Pretty Printing using pprint() and pformat()
import pprint
pprint.pprint(spam)
print(pprint.pformat(spam)) #it will kind of pre tag in html

