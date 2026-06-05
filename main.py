while True :
    # Choix du niveau de difficulté
    print("\n Voici les différents niveau du jeu mystère : \n")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile\n")
    choix = input("Quel est votre choix ?  ")

    if choix == "1":
        max_nombre = 50
        tentative_max = 4
    elif choix == "2":
        max_nombre = 100
        tentative_max = 6
    else :
        max_nombre = 1000
        tentative_max = 10

    # l'ordinateur choisit un nombre
    import random
    nbr_mystere = random.randint(1, max_nombre)
    essaie = 0
    i = 1

    # Le joueur propose un nombre, Comparaison, programme continue jusqu'à ce qu'il trouve.
    print("\nVeillez saisir un nombre compris entre 1 et",max_nombre,
    ". (","Vous n'avez que",tentative_max,"tentatives.)")

    while essaie < tentative_max :
        essaie += 1
        # Gestion des erreurs
        try:
            print("essai Num.",i," : ")
            nbre = int(input(""))
        except:
            print("Veuillez saisir un nombre.")

        if nbre < nbr_mystere :
            print("Oups, trop petit")
        elif nbre > nbr_mystere :
            print("Oups, trop grand")
        else :
            print("Gagné !")
            break
        i += 1

    if nbre != nbr_mystere :
        print(f"\nPerdu, le nombre était {nbr_mystere}")
    else :
        print("\nVous êtes très fort !")
        
    rejouer = input("\nDésirez-vous rejouer ? (oui/non): ").lower()
    if rejouer != "oui":
        print("Mercie d'avoir joué.")
        break
