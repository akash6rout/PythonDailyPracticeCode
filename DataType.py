total_bikes = 75
print(type(total_bikes))

bike_price = 79000.0
print(type(bike_price))

customer_name = "akash"
print(type(customer_name))

is_available = True
print(type(is_available))

available_models = ["TVS Jupiter","TVS Ntorq","TVS Raider"]
print(type(available_models))#list

showroom_timings = ("9:00 AM","8:00 PM")#fixed data no change
print(type(showroom_timings))#tuple

bike_color = {"Red","Blue","Black","Red"}# Duplicate auto remove not allowed
print(type(bike_color))#set

customer = {
    "name": "Manoj Lenka",
    "bike_model":"Tvs jupiter",
    "mobile":"887874834",
    "down_payment":30000,
    "loan_year":3
}
print(type(customer))

a = "10"
b = "20"
print(a+b)

bike_model = "TVS Ntorq"
# Hum direct model name badal nahi sakte
# Lekin naya model bana sakte hain
bike_model = bike_model.replace("V", "M")
print(bike_model)
