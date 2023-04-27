#slowniki
author = {
    'first_name': "Zofia",
    'last_name': "Nalokowska"
}
print(author['first_name'])
print(author['last_name'])

#wyswietla klucze
for item in author:
    print(item)

#wyswielka wartosci kluczy:
for item in author:
    print(item, author[item])

#other options:
print(author.items())
print(author.keys())
print(author.values())

#loop with item method
for item in author.items():
    print(item[0],item[1])
    
#another loop with item method
for first_name, last_name in author.items():
    print(first_name, last_name)
