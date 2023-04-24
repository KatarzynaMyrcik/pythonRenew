#key value pairs  -  dictonary. each key must be unique, value can be everything
customer = {
    "name": "John Smith",
    "age":30,
    "is_verified": True
}
#shows the value of name
print(customer["name"])
#in case of error(no key/value) all code is KO:
#print(customer["nae"])
#in case of error return value None
print(customer.get("nam"))
# if i write 2 values and the key doesn't exist it returns second value as a answer
print(customer.get("nam", "Johnny smiths"))
#how to change a value:
customer["name"] = "Olala Smith"
print(customer.get("name"))
#to add a new key:
customer["Birthdate"] = "01/12/1956"
print(customer.get("Birthdate"))
