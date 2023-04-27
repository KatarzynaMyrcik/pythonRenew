''' first simple exemple:
def calculate_sum():
    a = 2
    b = 3
    print("suma a + b", a + b)


calculate_sum()
'''
'''#second exemple where fonction takes 2 arguments:
def calculate_sum(a,b):
    print("suma a + b =", a + b)


calculate_sum(2,6)
'''
'''#second exemple where fonction takes 2 arguments and use wartosc domyslna c:
def calculate_sum(a,b, c=3):
    print("suma a + b =", a + b + c)
    return a + b + c


result = calculate_sum(2, 6)
#value c is changed here
calculate_sum(2,6,1)
print("wynik fukcji to", result)
'''
#argumenty funkcji pozycyjne - przekazujemy je w kolejnosci wedlug deklaracji:
#calculate_sum(2,6,1)
#nazwane - kolejnosc dowolna, posluguja sie nazwa
#calculate_sum(a = 2,b = 6,c = 1)
def calculate_sum(a = 1,b = 2, c=3):
    print("suma a + b =", a + b + c)
    return a + b + c


result = calculate_sum()
