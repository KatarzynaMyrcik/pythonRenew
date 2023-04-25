def greetings(first_name, last_name):
    print(f"""HI {first_name} {last_name}!
Welcome aboard""")


print("start")
greetings("John", "Jajo")
#position arguments in fonction
greetings(last_name = "Klaczek", first_name = "Mary")
print("finish")
