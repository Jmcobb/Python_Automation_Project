# Welcome to the main script. 
import func

# Welcome the user. 
print('Hello, User!')
print('Welcome to my code project.')
func.nl()

# Start list of criteria.
print('This program was built to meet the following criteria: ')
func.nl()

# pt.1
print('1. You will be able to run the program!')
func.yes_or_no()
func.nl()

#pt.2 
print('2. You will be able to deploy a VM, based on a given YAML file.')
func.create_vm()
func.nl()

#pt.3
print('3. You will be able to SSH into the new instance as user1 and user2.')
func.create_users()
func.verify_task()
func.nl()

#pt.4 
print('4. Read and write from the two volumes attached to the VM instance.')
func.verify_task()
func.nl() 

# Clean up.
print("Well that's all folks! If I were you, my next move would be to clean up the instances. If not they will still be running in your AWS account.")
func.clean_up()
func.nl()

# Send off.
print("I hoped you enjoyed my project, then next steps are to send me a job offer! Thanks again!")