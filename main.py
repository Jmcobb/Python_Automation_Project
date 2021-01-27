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

print('2. Next, you will be able to deploy a VM, based on a given YAML file.')
func.create_vm()
func.nl()

print('3. You will be able to SSH into the new instance as new_user1 and new_user2.')
func.nl()

print('4. Read and write from the two volumes attached to the VM instance.')
func.nl()