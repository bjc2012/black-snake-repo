import random
import string
import sys

# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.

#1 Create Function
def generate_string(size=6, string=string.ascii_letters + string.digits):    
    return ''.join(random.choice(string) for _ in range(size))
    
department = input("Please select Department: Accounting FinOps, Marketing: ")  

for _ in department:

    if department == "Marketing" or department.lower() == "marketing" :
        print("Success!")
        #print ("Marketing")
        break

    elif department == "Accounting" or department.lower() == "accounting" :
        print("Success")
        #print("Accounting")
        break

    elif department == "FinOps" or department.lower() == "finops" :
        print("Success!")
        #print("FinOps")
        break

    else:
        print("Error: Invalid entry. Please ensure correct department is selected.")
        raise SystemExit
        sys.exit()    
    
#2 Configure for number of EC2 instances requested
number = int(input("Enter the number of EC2 instances you need: ")) 

if number < 0:    
    print("Please select a positive number: ") 
elif number > 0:    
    print("Success!")
    
print()
print("--------------------------------")
print("EC2 Instance Names")
print("--------------------------------")
print() 
for _ in range(1, number + 1):    
    random_name = department    
    EC2_random_name = random_name + "-" + generate_string()
    print("Your EC2 Instance's random name is : ", EC2_random_name)    