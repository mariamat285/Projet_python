def  rechercher_patient(patients_valides, critere, valeur):
    if critere in ["id", "nom", "prenom", "age", "telephone", "ville", "groupe_sanguin", "poids", "taille"]:
        resultat = []
        for patient in patients_valides:
            if valeur.lower() in str(patient[critere].lower()):
                resultat.append(patient)
        return resultat
    else:
        print(f"valeur indisponible")
    return []
               
 