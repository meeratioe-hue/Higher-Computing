PetPurchased = ["Dog", "Dog", "Cat", "Rabbit", "Hamster", "Cat", "Hamster", "Budgie"]
AllUsers = []
PositionOfUser = 0
TargetAnimal = "Cat"


for i in range (len(PetPurchased)):
    if PetPurchased[i] == TargetAnimal:
        print ("position:", PositionOfUser)
    else:
        AllUsers.append [i+1]
   



