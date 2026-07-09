def convertir_longueur(valeur, de, vers):
    # Tout convertir en mètres d'abord
    en_metres = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "mile": 1609.344,
        "pied": 0.3048,
        "pouce": 0.0254
    }
    if de not in en_metres or vers not in en_metres:
        return "Unité inconnue"
    return valeur * en_metres[de] / en_metres[vers]

def convertir_masse(valeur, de, vers):
    en_kg = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "tonne": 1000,
        "livre": 0.453592,
        "once": 0.0283495
    }
    if de not in en_kg or vers not in en_kg:
        return "Unité inconnue"
    return valeur * en_kg[de] / en_kg[vers]

def convertir_temperature(valeur, de, vers):
    # Convertir vers Celsius d'abord
    if de == "celsius":
        celsius = valeur
    elif de == "fahrenheit":
        celsius = (valeur - 32) * 5/9
    elif de == "kelvin":
        celsius = valeur - 273.15
    else:
        return "Unité inconnue"

    # Convertir Celsius vers la cible
    if vers == "celsius":
        return celsius
    elif vers == "fahrenheit":
        return celsius * 9/5 + 32
    elif vers == "kelvin":
        return celsius + 273.15
    else:
        return "Unité inconnue"

def convertir_energie(valeur, de, vers):
    en_joules = {
        "joule": 1,
        "kjoule": 1000,
        "calorie": 4.184,
        "kcalorie": 4184,
        "kwh": 3600000,
        "ev": 1.602e-19
    }
    if de not in en_joules or vers not in en_joules:
        return "Unité inconnue"
    return valeur * en_joules[de] / en_joules[vers]

def afficher_menu():
    print("\n╔══════════════════════════════╗")
    print("║    Convertisseur d'Unités    ║")
    print("╠══════════════════════════════╣")
    print("║  1. Longueur                 ║")
    print("║  2. Masse                    ║")
    print("║  3. Température              ║")
    print("║  4. Énergie                  ║")
    print("║  0. Quitter                  ║")
    print("╚══════════════════════════════╝")

def choisir_unite(unites):
    print("\nUnités disponibles :")
    for i, u in enumerate(unites, 1):
        print(f"  {i}. {u}")
    choix = int(input("Ton choix : ")) - 1
    return unites[choix]

def main():
    historique = []

    unites_longueur = ["km", "m", "cm", "mm", "mile", "pied", "pouce"]
    unites_masse = ["kg", "g", "mg", "tonne", "livre", "once"]
    unites_temperature = ["celsius", "fahrenheit", "kelvin"]
    unites_energie = ["joule", "kjoule", "calorie", "kcalorie", "kwh", "ev"]

    while True:
        afficher_menu()
        choix = input("\nTon choix : ")

        if choix == "0":
            print("\nAu revoir !")
            break

        elif choix in ["1", "2", "3", "4"]:
            valeur = float(input("\nValeur à convertir : "))

            if choix == "1":
                print("\nUnité de départ :")
                de = choisir_unite(unites_longueur)
                print("\nUnité d'arrivée :")
                vers = choisir_unite(unites_longueur)
                resultat = convertir_longueur(valeur, de, vers)

            elif choix == "2":
                print("\nUnité de départ :")
                de = choisir_unite(unites_masse)
                print("\nUnité d'arrivée :")
                vers = choisir_unite(unites_masse)
                resultat = convertir_masse(valeur, de, vers)

            elif choix == "3":
                print("\nUnité de départ :")
                de = choisir_unite(unites_temperature)
                print("\nUnité d'arrivée :")
                vers = choisir_unite(unites_temperature)
                resultat = convertir_temperature(valeur, de, vers)

            elif choix == "4":
                print("\nUnité de départ :")
                de = choisir_unite(unites_energie)
                print("\nUnité d'arrivée :")
                vers = choisir_unite(unites_energie)
                resultat = convertir_energie(valeur, de, vers)

            print(f"\n✓ {valeur} {de} = {round(resultat, 6)} {vers}")
            historique.append(f"{valeur} {de} → {round(resultat, 6)} {vers}")

        else:
            print("\nChoix invalide, réessaie.")
            continue

        voir = input("\nVoir l'historique ? (o/n) : ")
        if voir == "o":
            print("\n--- Historique ---")
            for i, op in enumerate(historique, 1):
                print(f"  {i}. {op}")

if __name__ == "__main__":
    main()