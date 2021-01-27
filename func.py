# Here is to show my logic skills w/ python! 

# Also, here is an example of good practice which results in 
# cleaner code by having a module containing this python functions.

import auto_build
import boto3

def nl(): 
    print('\n')

def yes_or_no():
    print('Are you running the program? y/n')
    x = input('response: ')
    if x[-1] == 'y':
        print('Good, time to get to the fun part!')
    elif x[-1] == 'n':
        print('Lol, I am glad to see you have a sense of humor.')
        nl()
        yes_or_no()
    else:
        print('That does not seem like an option to me... Try again!')
        nl()
        yes_or_no() 

# I hope whoever grades this laugh as much as I did. 

def create_vm(): 
    print('Time to create a VM based on the YAML provided.')
    