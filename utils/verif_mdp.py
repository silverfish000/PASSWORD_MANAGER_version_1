def verif_mdp(mot_de_passe, dictionnaire):
    
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caracteres"
    

    majuscule_trouve = False

    for lettre in mot_de_passe:
        if lettre.isupper():
            majuscule_trouve = True
            break

    if not majuscule_trouve:
        return False, "Doit contenir au moins une majuscule"
    

    minuscule_trouve = False

    for lettre in mot_de_passe:
        if lettre.islower():
            minuscule_trouve = True
            break

    if not minuscule_trouve:
        return False, "Doit contenir au moins une minuscule"


    caracteres_speciaux = "!@#$%^&*()_+-=?/"
    special_trouve = False

    for caractere in mot_de_passe:
        if caractere in caracteres_speciaux:
            special_trouve = True
            break
        
    if not special_trouve:
        return False, "Doit contenir au moins un caractere special"
    

    for cle in dictionnaire:
        if cle != 'categories_mot_de_passe':
            if dictionnaire[cle] == mot_de_passe:
                return False, "Ce mot de passe existe deja"
    
    return True, "Mot de passe valider"


def demander_mdp_valide(categorie_nom, dictionnaire):
    while True:
        nouveau_mdp = input(f"Entre le mot de passe pour {categorie_nom} : ")
        valide, message = verif_mdp(nouveau_mdp, dictionnaire)
        
        if valide:
            print()
            print(f" {message}")
            return nouveau_mdp
        else:
            print()
            print(f" Erreur : {message}")
            print()
            print("Recommence !")
            print()