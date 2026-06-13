#-----------------NOMBRE TOTAL PATIENT BRUT--------------------------- 
def patient_total(patients_valides, patients_rejetes):
    nbr_total_patient = len(patients_valides) + len(patients_rejetes) 
    return nbr_total_patient
#----------------NOMBRE DE PATIENT VALIDES----------------------------
def nombre_valides(patients_valides):
    return len(patients_valides)
#----------------NOMBRE DE PATIENT REJETER-----------------------------
def patients_rejetes(patients_rejetes):
    return len(patients_rejetes)
#--------------MOYENNE AGE VALIDE--------------------------------------
def moyenne_age(patients_valides):
    if len(patients_valides) == 0:
        return 0
    somme = 0
    for patient in patients_valides:
        somme += float(patient["age"])
    return somme/len(patients_valides)
#-------------------MOYENNE POIDS VALIDE------------------------------
def moyenne_poids(patients_valides):
    if len(patients_valides) == 0:
        return 0
    somme = 0
    for patient in patients_valides:
        somme += float(patient["poids"])
    return somme/len(patients_valides)
#------------------VILLE PLUS FREQUENTE-------------------------------------
def ville_frequente(patients_valides):
    compteur = {}
    for patient in patients_valides:
        ville = patient["ville"]
        if ville in compteur:
            compteur[ville] += 1
        else:
            compteur[ville] = 1
    return max(compteur, key=compteur.get)
#-----------------REPARTITION GROUPE SANGUIN------------------------------
def groupe_sanguin(patients_valides):
    compteur = {}
    for patient in patients_valides:
        groupe_sanguin = patient["groupe_sanguin"]
        if groupe_sanguin in compteur:
            compteur[groupe_sanguin] += 1
        else:
            compteur[groupe_sanguin] = 1
    return compteur