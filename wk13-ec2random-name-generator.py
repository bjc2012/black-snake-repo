import random
import string
import sys

# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.

def generate_string(names, department):
  name = []
  for i in range(names):
    name = department + '-'
    for t in range(6):
      name += random.choice(string.ascii_letters + string.digits)
    names.append(name)
  return names

# Run Function
names = int(input("Please select the number of EC2 names you want: "))
department = input("Please select your department name: ")

names = generate_string(names, department)
for name in names:
  print(name)
  


