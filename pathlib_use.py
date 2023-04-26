from pathlib import Path

#Absolute path
#relative path

#to check if directory exist:
#path = Path("email")
#print(path.exists())
#to add a new directory:
#path.mkdir()
#to delete:
#path.rmdir()
#to search directory or file in curent path

path = Path()
#print(path.glob("*.*")) #files
#print(path.glob("*.py"))

for file in path.glob("*.py"):
    print(file)
