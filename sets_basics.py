#zbiory set
first_names = set()
first_names.add("michal")
first_names.add("john")
first_names.add("adam")
first_names.add("john")
first_names.add("adamiec")
#kolejnosc w zbiorach jest bez znaczenia. sa jak worek z prezentami.
print(first_names)

#how to change a list to a set
kuku = ["dsadsa", "onono", "onono", "jajaa"]
print(kuku)
ukuk = set(kuku)
print(ukuk)


team_a = {"wojtek", "adam", "rafal", "kon", "zenek", "omar"}
team_b = {"natasha", "oliwia", "omar", "mosh", "zenek"}
print("suma", team_a | team_b)
print("roznica a - b", team_a - team_b)
print("roznica b - a", team_b - team_a)
print("iloczyn (wspolna czesc)", team_a & team_b)
print("roznica symetryczna (minus wspolna czesc)", team_a ^ team_b)
