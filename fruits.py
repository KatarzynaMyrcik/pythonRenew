fruits = []

for i in range(5):
    fruits.append(input(f"Jaki jest Twoj {i+1} ulubiony owoc: "))

print(f'OK. dziekuje. no to mozemy zrobic salatke z: {fruits}. Bedziemy uzywac ich w nastepujacej kolejnosci:')
for fruit in fruits:
    print(fruit)
