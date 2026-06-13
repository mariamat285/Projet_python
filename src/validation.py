#--------------VALIDER TELEPHONE---------------------#
def telephone_valide(telephone):
    if len(telephone) == 9 and telephone.startswith("7") and telephone.isdigit():
        return True
    return False
#--------------------VALIDER TAILLE------------------------#
def taille_valide(taille):
    try:
        taille = float(taille)
        if float(taille) >= 50 and float(taille) <= 250:
            return True
    except ValueError:
        return False
    return False
#---------------VALIDER POIDS-----------------------#
def poids_valide(poids):
    try:
        poids = float(poids)
        return 1 <= poids <= 300
    except ValueError:
        return False