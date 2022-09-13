#EC2 Random Name Generator
import random
import string

#Departments sharing an AWS environment
dept = ['Sales', 'Shipping', 'Receiving', 'Delivery', 'HR', 'Admin']

#User inputs the amount of EC2s needed
ec2_instances = int(input("How many instances will you need to run? "))

#User will list their department
dept = str(input("What department are you in? "))

#Random characters and numbers that will be generated and included in the unique name for EC2
char_numb = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10))
print(char_numb)

#Selected department and EC2 is my unique name
print((dept + '_' + char_numb) + ' ' + 'is my EC2 name')