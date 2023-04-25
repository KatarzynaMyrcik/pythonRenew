def greetings(first_name, last_name):
    print(f"""HI {first_name} {last_name}!
Welcome aboard""")


print("start")
#position arguments
greetings("John", "Jajo")
#keyword arguments in fonction. If e have position and keyword arguments together we have to use position arguments first, and then keyword arguments
greetings(last_name = "Klaczek", first_name = "Mary")
print("finish")
