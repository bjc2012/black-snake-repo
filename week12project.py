# 1) Create an empty list of AWS services


aws_services = []

# 2) Populate the list using append and/or insert

aws_services.append('Python')
aws_services.append('CloudFormation')
aws_services.append('Kubernetes')
aws_services.insert(3, 'S3')
aws_services.insert(4, 'Lambda')
aws_services.insert(5, 'Cloud9')


# 3) Print the list and length of the list
print(aws_services)
print(len(aws_services))




