# Welcome to the main script. 
import func

print('Hello, User!')
print('Welcome to my code project.')
func.nl()
print('This program was built to meet the following criteria: ')
func.nl()
print('1. You will be able to run the program!')
func.yes_or_no()
func.nl()
print('2. You will be able to deploy a VM, based on a given YAML file.')
func.create_vm()
func.nl()
print('3. You will be able to SSH into the new instance as user1 and user2.')
func.create_users()
func.verify_task()
func.nl()
print('4. Read and write from the two volumes attached to the VM instance.')
func.verify_task()
func.nl() 
print("Well that's all folks! If I were you, my next move would be to clean up the instances. If not they will still be running in your AWS account.")
func.clean_up()
func.nl()
print("I hoped you enjoyed my project, then next steps are to send me a job offer! Thanks again!")