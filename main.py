from random import randint
x=randint(1,1000)
print(x)
jeu= True
while jeu :
    y = int(input("enter un nombre entre 1 et 1000"))
    if x==y :
        print("vous avez gagné")
        jeu=False



    elif x < y :
        print("c'est plus  ")
    elif x > y:
        print("c'est moins ")



