
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

#--------------VALIDER GROUPE SANGUIN---------------------
def groupe_sanguin_valide(groupe):
    
    groupes_valides = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+","O-"]

    if groupe.strip() not in groupes_valides:
        return False
    return True
#--------------VALIDER AGE---------------------#
def age_valide(age):

    if not age.isdigit():
        return False
    if int(age) > 120  :
        return False
    if int(age) == 0:
        pass
    return True
#-----------------VALIDER NOM---------------------------------#
def nom_valide(nom):
    if nom == "":
        return False
    return True
#-----------------VALIDER PRENOM------------------------------------#
def prenom_valide(prenom):
    if prenom == "":
        return False
    return True 
#-----------------TELEPHONE SUSPECT------------------------------#
def telephone_suspect(telephone):

    telephone = list(telephone)
    if len(telephone) >= 9:
        if telephone[2] == telephone[3] == telephone[4]== telephone[5] == telephone[6] == telephone[7] == telephone[8]:
            return True
        return False
#-----------------DETECTER ANOMALIES-----------------------------#   
def detecter_anomalies(patients):
    for patient in patients:
        if not groupe_sanguin_valide(patient['groupe_sanguin'] ):
            print(f"Le patient {patient['id']} son groupe sanguin {patient['groupe_sanguin']} n'est pas valide")
        if not age_valide(patient['age']):
            print(f"Le patient {patient['id']} son age  {patient['age']} n'est pas valide")
        if not telephone_valide(patient['telephone']):
            print(f"Le patient {patient['id']} son numéro de téléphone {patient['telephone']} n'est pas valide")
        if not taille_valide(patient['taille']):
            print(f"Le patient {patient['id']} sa taille {patient['taille']} n'est pas valide")
        if not poids_valide(patient['poids']):
            print(f"Le patient {patient['id']} son poids {patient['poids']} n'est pas valide")
        if not nom_valide(patient['nom']):
            print(f"Le patient {patient['id']} son nom est manquant")
        if not prenom_valide(patient['prenom']):
            print(f"Le patient {patient['id']} son nom est manquant")
        if telephone_suspect(patient['telephone']):
            print(f"Le patient {patient['id']} son numéro de téléphone ({patient['telephone']}) est suspect")
        if patient['age'] == 0:
            print(f"Le patient {patient['id']} son age  ({patient['age']}) est suspect")

