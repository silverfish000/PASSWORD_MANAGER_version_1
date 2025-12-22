import string

def verif_mdp(mot_de_passe, dictionnaire):
    
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractere"
    
    if not any(c.isupper() for c in mot_de_passe):
        return False, "Doit contenir au moins une majuscule"
    
    if not any(c.islower() for c in mot_de_passe):
        return False, "Doit contenir au moins une minuscule"
    
    if not any(c in string.punctuation for c in mot_de_passe):
        return False, "Doit contenir au moins un caractere special"
    
    for cle, valeur in dictionnaire.items():
        if cle != 'categories_mot_de_passe' and valeur == mot_de_passe:
            return False, "Ce mot de passe existe dejaa"
    
    return True, "Mot de passe valide"
