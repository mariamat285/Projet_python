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

    villes = [
        "Dakar", "Thiès", "Saint-Louis", "Kaolack", "Ziguinchor",
        "Diourbel", "Fatick", "Kolda", "Louga", "Matam",
        "Kaffrine", "Kédougou", "Sédhiou","Tambacounda"
    ]

    ville = ville.lower().strip()

    meilleure_ville = ""
    min_diff = 10

    for v in villes:
        v_test = v.lower().strip()

        # différence de longueur
        diff = abs(len(ville) - len(v_test))

        # comparaison lettre par lettre
        for i in range(min(len(ville), len(v_test))):
            if ville[i] != v_test[i]:
                diff += 1

        # garder la meilleure ville
        if diff < min_diff:
            min_diff = diff
            meilleure_ville = v

    # vérification finale
    if min_diff < len(meilleure_ville) / 2:
        return meilleure_ville
    else:
        return "Ville inconnue"
    
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
    for patient in patients_valides:
        if patient not in liste_propre:
            liste_propre.append(patient)
        else:
            doublons.append(patient)
    return doublons, liste_propre

    








































