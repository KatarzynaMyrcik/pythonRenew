weight = input('Give me please your weight: ')
type = input("Could you please write if it is a weight in kg or pounds? For kg please type [K], for pounds please type [P] ")
#1 pound it is 0.45359237 kg

#print(type)
low_type = type.lower()
#print(low_type)

if low_type == 'p':
    pdweight = float(weight) / 0.45
    print(str(round(pdweight, 1)) + '  is your weight in kg')
elif low_type == 'k':
    pdweight = float(weight) * 0.45
    print(str(round(pdweight, 1)) + '  is your weight in pounds')
else:
    print('hmmm. Something went wrong. Maybe it was your cat clicking on the keyboard...')
