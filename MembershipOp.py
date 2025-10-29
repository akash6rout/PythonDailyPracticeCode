#List of active gym members
members = ["AKASH","MANOJ","LENKA","PRABHU"]

#take user name as input
name = input("Enter your name :")

#check membership status using 'in' operator
if name in members:
    print("you are active",name)
else:
    print("you are not ",name)