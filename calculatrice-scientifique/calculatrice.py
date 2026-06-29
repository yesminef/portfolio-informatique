import math

def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def puissance(a, b):
    return a ** b

def racine(a):
    if a < 0:
        return "Erreur : racine d'un nombre négatif"
    return math.sqrt(a)

def afficher_menu():
    print("\n╔══════════════════════════════╗")
    print("║   Calculatrice Scientifique  ║")
    print("╠══════════════════════════════╣")
    print("║  1. Addition                 ║")
    print("║  2. Soustraction             ║")
    print("║  3. Multiplication           ║")
    print("║  4. Division                 ║")
    print("║  5. Puissance                ║")
    print("║  6. Racine carrée            ║")
    print("║  0. Quitter                  ║")
    print("╚══════════════════════════════╝")

def main():
    historique = []

    while True:
        afficher_menu()
        choix = input("\nTon choix : ")

        if choix == "0":
            print("\nAu revoir !")
            break

        elif choix in ["1", "2", "3", "4", "5"]:
            a = float(input("Premier nombre : "))
            b = float(input("Deuxième nombre : "))

            if choix == "1":
                resultat = additionner(a, b)
                operation = f"{a} + {b}"
            elif choix == "2":
                resultat = soustraire(a, b)
                operation = f"{a} - {b}"
            elif choix == "3":
                resultat = multiplier(a, b)
                operation = f"{a} × {b}"
            elif choix == "4":
                resultat = diviser(a, b)
                operation = f"{a} ÷ {b}"
            elif choix == "5":
                resultat = puissance(a, b)
                operation = f"{a} ^ {b}"

            print(f"\nRésultat : {operation} = {resultat}")
            historique.append(f"{operation} = {resultat}")

        elif choix == "6":
            a = float(input("Nombre : "))
            resultat = racine(a)
            operation = f"√{a}"
            print(f"\nRésultat : {operation} = {resultat}")
            historique.append(f"{operation} = {resultat}")

        else:
            print("Choix invalide, réessaie.")

        voir_historique = input("\nVoir l'historique ? (o/n) : ")
        if voir_historique == "o":
            print("\n--- Historique ---")
            for i, op in enumerate(historique, 1):
                print(f"  {i}. {op}")

if __name__ == "__main__":
    main()