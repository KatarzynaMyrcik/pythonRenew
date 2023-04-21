has_high_income = True
has_good_credit = False
has_criminal_record = False

#test of not operator
if has_high_income and not has_good_credit and not has_criminal_record:
    print("you can ask for a credit")
    
#at least one condition sould be true:
if has_high_income or has_good_credit:
    print("you can ask for loan")

#both conditions should be true:
if has_high_income and has_good_credit:
    print("eligible for loan")
