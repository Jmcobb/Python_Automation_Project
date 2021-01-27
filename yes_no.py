# Here is to show some basic logic w/ python! 

# Also, here is an example of good practice which results in 
# cleaner code by having a module containing this python function.
# I believe it is called "Seperation of Concerns"

def yes_or_no():
    print('Are you running the program? y/n')
    x = input('response: ')
    if x[-1] == 'y':
        print('Good, time to get to the fun part!')
    elif x[-1] == 'n':
        print('Lol, I am glad to see you have a sense of humor.')
        yes_or_no()
    else:
        print('That does not seem like an option to me... Try again!')
        yes_or_no()

# I hope whoever grades this laugh as much as I did. 