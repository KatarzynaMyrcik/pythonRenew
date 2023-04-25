translation = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:'six',
    7:"seven",
    8:"eight",
    9:"nine",
    0:"zero"
}
output = ""
phone_number = input("Could you please give me your phone number? ")
#number = str(23412)
for number in phone_number:
    output += translation.get(int(number), "oo") + " "
print(output)
