birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True : 
    print('Enter a name (keep blank if you want to terminate this program)')
    name = input();
    if name == '':
        break;
    else :
        if name in birthdays:
            print (birthdays[name] + ' is ' + name + ' birthday.')
        else :
            print("In Brith day database no data found for " + name + ". when is the Birthday of " + name + " ?")
            bday = input();
            birthdays[name] = bday;
            print('Birthdays database updated')



