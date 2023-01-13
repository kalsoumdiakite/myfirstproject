tableau=[]
for i in range(10):
 n= int(input("Entrer un nombre compris entre 0 et 20"))
 while n < 0 or n > 20 :
     n=int(input("Entrer un nombre valide compris entre 0 et 20"))
 tableau.append(n)
 first= []
 second = []
 third= []

for n  in tableau:
    if n < 10 :
        first.append(n)
for n in tableau:
    if n >= 10 and  n < 15 :
        second.append(n)

for n in tableau:
    if n >= 15 and n <= 20:
        third.append(n)

print("le nombre de valeurs inferieures à 10 est {}".format(len(first)))
print("le nombre de valeurs supérieures ou eagles à 10 et inferieurs à 15 sont {}".format(len(second)))
print("le nombre de valeurs superieures ou egales à 15 sont {}".format(len(third)))







