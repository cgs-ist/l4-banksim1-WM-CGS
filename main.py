# Non OOP
# Bank Version 1
# Single Account
from PIL import Image
img = Image.open("assets/dog.png")

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
    
    action = input("What do you want to do? ")
    action = action.lower() #lowercasing letters
    action = action[0] #getting the first thing entered i.e ( if "withdraw" is entered, only "w" will go thru)
    
    if action == 'b': #double equal is a comparitor, single equal is an assignment
        print('Get Balance:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword: #comparitor that checks if something does NOT equal
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)

    elif action == 'w':
        print('Withdraw:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword: #comparitor that checks if something does NOT equal
            print('Incorrect Password')
        else:
            temp = float(input('How much would you like to withdraw? '))
            accountBalance = accountBalance - temp
            print('Your balance is: ', accountBalance)

    elif action == 'd':
        print('Deposit:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword: #comparitor that checks if something does NOT equal
            print('Incorrect Password')
        else:
            temp = float(input('How much would you like to Deposit? '))
            accountBalance = accountBalance + temp
            print('Your balance is: ', accountBalance)
        
    elif action == 's':
        print('Show Account:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword: #comparitor that checks if something does NOT equal
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance, '|', 'Under the name of: ', accountName, '|', 'With the password of: ', accountPassword)

    elif action == 'q':
        print('Have a nice day :)')
        img.show()
        break

    else:
        print("please input an executable action")