#String Literals 
'hello world'

#double quote. benifit of double quote is it can hold single quote
spam = "That is Alice's cat."

#Escape Characters (\)
spam = 'Say hi to Bob\'s mother.'
\' Single quote
\"Double quote
\t Tab
\n Newline (line break)
\\ Backslash

#Raw Strings
print(r'That is Carol\'s cat.') >>> That is Carol\'s cat.

#Multiline sting
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

#Multiline Comments
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

#Indexing and Slicing Strings
spam = 'Hello world!'
spam[0] >>> H 
spam[-1] >>> !
spam[0:5] / spam[:5] >>> Hello
spam[6:] >>> world

#in and not in Operator
'Hello' in 'Hello World' >>> True
'cats' not in 'cats and dogs' >>> False

#upper(), lower(), isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle()
spam = 'Hello world!'
spam.upper() >>> 'HELLO WORLD!'
spam.islower() >>> False

#startswith() and endswith() 
'Hello world!'.startswith('Hello') >>> True

#join() and split() 
', '.join(['cats', 'rats', 'bats'])  >>> 'cats, rats, bats'
'ABC'.join(['My', 'name', 'is', 'Simon']) >>> 'MyABCnameABCisABCSimon'
'My name is Simon'.split()  >>> ['My', 'name', 'is', 'Simon'] // if nothing specified as arguments whenever whitespace or new line is found it will break
'MyABCnameABCisABCSimon'.split('ABC') >>> ['My', 'name', 'is', 'Simon']

# some peculiar method. rjust(), ljust(), and center()
'Hello'.rjust(10) >>> '     Hello'
'Hello'.rjust(20, '*') >>> '***************Hello'
'Hello'.center(20, '=') >>> '=======Hello========'

#Removing Whitespace with strip(), rstrip(), and lstrip()
spam = '    Hello World     ' >>> Hello World
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('Spam') >>> BaconSpamEggs
spam.strip('pSam') >>> BaconSpamEggs //order inside arguments doesn't matter

#third party pyperclip
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste() >>> Hello World

