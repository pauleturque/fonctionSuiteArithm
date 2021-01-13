def calcul(u0, r, nb):
    terme = u0
    somme = 0
    for k in range(nb):
        somme += terme
        terme += r
    return somme

u0 = int(input("Entrez le premier terme de la suite : "))
r = int(input("Entrez la raison de la suite : "))
nb = int(input("Entrez le nombre de termes de la suite : "))

print("La somme de cette suite est = ", calcul(u0, r, nb))
