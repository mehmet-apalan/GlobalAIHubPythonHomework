name=input("Your name: ")
surname=input("Your surname: ")
age=input("Your age: ")
birth=input("Your birth year: ")

liste=[name,surname,age,birth]

for i in liste:
    print(i)

if int(liste[2])<18:
    print("You can't go out because it's so dangerous")
else:
    print("You can go out the street")