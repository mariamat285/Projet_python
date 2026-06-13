#-------FONCTION CHARGEMENT DE FICHIER--------#
def chargement(fichier):
    try:
        with open(fichier, 'r', encoding = "UTF-8") as contenu:

            patients = []

            
            next(contenu)#ignorer l'entete

            for ligne in contenu:
                
                element = ligne.strip().split(";")
                
                if len(element) == 9:   
                    try:
                        patient = {
                            "id":element[0],
                            "nom":element[1],
                            "prenom":element[2],
                            "age":element[3],
                            "telephone":element[4],
                            "ville":element[5],
                            "groupe_sanguin":element[6],
                            "poids":element[7],
                            "taille":element[8]
                        }
                        patients.append(patient)
                    except IndexError as e:
                        print(f"IndexError : {e}")
        return patients
    except  FileNotFoundError:
        print(f"Erreur : le fichier '{fichier}' est introuvable.")
        return []   

chargement("data/patients_bruts.txt")
