# Ajouter/Modifier/Supprimer des mots de passe
import os


# ------------ db de categories et tout les mots de passes (non chiffres) ------------
dictionnaire_test = {
    'categories_mot_de_passe' : ""
}
# ------------ FIN ------------


def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_choix() : # pour plus tard
    clear()
    print("-="*35)
    print("GESTIONNAIRE DES CHOIX UTILISATEURS (ONLY ADMIN)".center(65))
    print("-="*35)
    print()


def aff_menu() :
    clear()
    print("-="*35)
    print("GESTIONNAIRE DE MOT DE PASSE".center(65))
    print("-="*35)
    print("by Silver & Squash\n")
    print("1) Ajouter un mot de passe\n")
    print("2) Modifier un mot de passe\n")
    print("3) Supprimer un mot de passe\n")
    while (True) :
        try :
            choix_user = int(input("Fais ton choix (QUE DES CHIFFRES) :"))
            break
        except ValueError :
            print("ERREUR : Tu ne dois que choisir des nombres")
    if (choix_user == 1) :
        print("Tu as choisis l'option 1")
    elif (choix_user == 2) :
        print("Tu as choisis l'option 2")
    else :
        print("Tu as choisis l'option 3")
    return choix_user



def add_mdp(choix_user, categorie) :
    if (choix_user == 1) :
        input("Choisis")
    elif (choix_user == 2) :
        print("Tu as choisis l'option 2")
    else :
        print("Tu as choisis l'option 3")
choix = aff_menu()

add_mdp(choix, dictionnaire_test)


# _0_