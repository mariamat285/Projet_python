#-------------METTRE TOUT LES NOMS EN TITTLE----------#
def nettoyer_nom(nom):
    nom = nom.strip().title()
    return nom
#-------------METTRE TOUT LES PRENOMS EN TITTLE----------#    
def nettoyer_prenom(prenom):
    prenom = prenom.strip().title()
    return prenom
#------------METTRE LES VILLE SOUS FORMAT CORRECT---------#
def nettoyer_ville(ville):
    corrections = {
        "dakarr": "Dakar",
        "dakkar": "Dakar",
        "saint louis": "Saint-Louis",
        "saint-louis": "Saint-Louis",  
        "ziguincor": "Ziguinchor",
        "ziginchor": "Ziguinchor",
        "kaolak": "Kaolack",
        "lougar": "Louga",
        "tamba": "Tambacounda",
        "diorbel": "Diourbel",
        "thiès": "Thies",
    }
    
    ville = ville.strip().title()
    
    if ville.lower() in corrections:
        ville = corrections[ville.lower()]
    
    return ville
#-------------NETTOYER TELEPHONE-------------#
def nettoyer_telephone(telephone):
    
    telephone = telephone.replace(" ", "").replace("-", "")

    if telephone.startswith("+221"):
        telephone = telephone[4:]
    elif telephone.startswith("00221"):
        telephone = telephone[5:]
    
    return telephone
#-------------NETTOYER AGE-------------#
def nettoyer_age(age):
    return age.strip()
#-------------NETTOYER POIDS-------------#
def nettoyer_poids(poids):
    return poids.strip()
#-------------NETTOYER TAILLE-------------#
def nettoyer_taille(taille):
    return taille.strip()
#-------------NETTOYER DOUBLONS-------------#
def nettoyer_doublons(patients_valides):
    liste_propre = []
    doublons = []
    vus = []
    
    for patient in patients_valides:
        cle = (patient['nom'].strip().lower(), patient['prenom'].strip().lower(), patient['telephone'].strip())
        if cle not in vus:
            vus.append(cle)
            liste_propre.append(patient)
        else:
            doublons.append(patient)
    
    return doublons, liste_propre

    









































