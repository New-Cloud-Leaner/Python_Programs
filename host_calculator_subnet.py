#This is crude python program is to calculate the number of hosts in a subnet in AWS VPC.
subnet_cidr_block = input("enter the cidr block of the subnet , example 10.0.0.0/24: ")
extract_cidr_number = int(subnet_cidr_block.split('/')[1])
if (extract_cidr_number > 28):
    print("Please enter the correct CIDR block , AWS doesn't support CIDR block more than 28 within a subnet")
else:
    print(f"thank you for confirming your CIDR number is: {extract_cidr_number}")
    extract_the_hosts_number = int((2**(32-extract_cidr_number))-5)
    print(f"The number of hosts or usable IPs available for you in AWS within a subnet is: {extract_the_hosts_number}")
    print("Thank you for using the subnet CIDR calculator!!!")
