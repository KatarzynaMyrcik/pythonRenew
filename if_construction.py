name = input("Could you please give me a name of your imaginary friend? ")

lenght = len(name)
print(lenght)

if lenght > 50:
    print("OOO, realy? It is too large. I'll forgot it")
elif lenght < 3:
    print("No way! You're so lazy to give so short name to your friend? I hope he is not offended. ")
else:
    print("Name looks good but if you have an imaginary friend something could be wrong with you. You should see a doctor!")
