#-------------NETTOYER TELEPHONE-------------#
def nettoyer_telephone(telephone):
    
    telephone = telephone.replace(" ", "").replace("-", "")

    if telephone.startswith("+221"):
        telephone = telephone[4:]
    elif telephone.startswith("00221"):
        telephone = telephone[5:]
    
    return telephone

#-------------NETTOYER POIDS-------------#
def nettoyer_poids(poids):
    return poids.strip()

#-------------NETTOYER TAILLE-------------#
def nettoyer_taille(taille):
    return taille.strip()