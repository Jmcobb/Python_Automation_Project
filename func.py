# Here is to show my logic skills w/ python! 

# Also, here is an example of good practice which results in 
# cleaner code by having a module containing this python functions.
import time
import auto_builder


def nl(): 
    time.sleep(1.5)
    print('\n')
    
def verify_task():
    nl()
    print('Were you able to verify the task? y/n')
    x = input('response: ')
    if x[-1] == 'y':
        print('Good, time to move on!')
    elif x[-1] == 'n':
        print('Lol, I am glad to see you have a sense of humor.')
        nl()
        verify_task()
    else:
        print('That does not seem like an option to me... Try again!')
        nl()
        verify_task() 

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
    auto_builder.create_instance()      
    
def create_users(): 
    print('Now that you have an instance, you want to make sure you they are up and running, so you can verify pt. 3.')
    print('Let us generate some useres so we can accomplish that!')
    auto_builder.create_user()
    print('Your users are created. You will now be able to open a separate terminal and SSH into the new instances to verify pt.3!')

def clean_up(): 
    print('Are you ready to close the instances?')
    x = input('response: ')
    if x[-1] == 'y':
        print('Alright, I am cleaning up now!')
        auto_builder.destroy_instance()
        auto_builder.destroy_user
    elif x[-1] == 'n':
        print('Alright, the instances will remain open for testing. Reminder: You will need to close these manually on your AWS account.')
        nl()
    else:
        print('That does not seem like an option to me... Try again!')
        nl()
        clean_up()