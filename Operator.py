#Membership Operater
# name = "Akash"

# print('A' in name)
# print('z' in name)
# print('z' not in name)

# bikes = ["Raider","Ntorq","Jupiter"]

# print("Raider" in bikes)
# print("Apache" not in bikes)

models = ["Apache","Ntorq","Raider","Jupiter"]
customer_choice= input("Enter Your Model.")

if customer_choice in models:
    print('Model available in stock!')
else:
    print("model not available.")