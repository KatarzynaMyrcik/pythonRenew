from finances import calculate_brutto

netto = float(input("Jaka jest twoja wartosc netto? "))
vat = float(input("Jaka jest twoja vat? "))
brutto = calculate_brutto(netto, vat)

#to see more details click on left ctrl and
print(f"Twoja wyplata to {brutto}")
