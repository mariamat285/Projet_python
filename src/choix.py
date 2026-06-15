from chargement import chargement
from export import export_csv, export_json, exporter_rapport
from nettoyage import nettoyer_age, nettoyer_doublons, nettoyer_nom, nettoyer_poids, nettoyer_prenom, nettoyer_taille, nettoyer_telephone, nettoyer_ville
from statistiques import patient_total, nombre_valides, moyenne_poids, moyenne_age, ville_frequente, groupe_sanguin
from validation import groupe_sanguin_valide, age_valide, telephone_valide, taille_valide, poids_valide, nom_valide, prenom_valide, detecter_anomalies
from recherche import rechercher_patient
from logs import log

#----------------------CHOIX 1 --------------------------#
def choix1(chemin):
    try:
        patients = chargement(chemin)
        log(f"Fichier chargé : {len(patients)} patients — {chemin}")
        return patients, chemin
    except Exception as e:
        log(f"Erreur chargement : {e}")
        return [], chemin

#----------------------CHOIX 2 --------------------------#
def choix2(chemin):
    try:
        patients, chemin = choix1(chemin)
        detecter_anomalies(patients)
        log("Anomalies affichées")
    except Exception as e:
        log(f"Erreur anomalies : {e}")
        print(f"Erreur : {e}")

#----------------------CHOIX 3 --------------------------#
def choix3(chemin):
    try:
        patients, chemin = choix1(chemin)
        patients_valides = []
        patients_rejetes = []
        for patient in patients:
            patient['prenom'] = nettoyer_prenom(patient['prenom'])
            patient['nom'] = nettoyer_nom(patient['nom'])
            patient['ville'] = nettoyer_ville(patient['ville'])
            patient['telephone'] = nettoyer_telephone(patient['telephone'])
            patient['age'] = nettoyer_age(patient['age'])
            patient['poids'] = nettoyer_poids(patient['poids'])
            patient['taille'] = nettoyer_taille(patient['taille'])

            if not groupe_sanguin_valide(patient['groupe_sanguin']):
                patients_rejetes.append(patient)
            elif not age_valide(patient['age']):
                patients_rejetes.append(patient)
            elif not telephone_valide(patient['telephone']):
                patients_rejetes.append(patient)
            elif not taille_valide(patient['taille']):
                patients_rejetes.append(patient)
            elif not poids_valide(patient['poids']):
                patients_rejetes.append(patient)
            elif not nom_valide(patient['nom']):
                patients_rejetes.append(patient)
            elif not prenom_valide(patient['prenom']):
                patients_rejetes.append(patient)
            else:
                patients_valides.append(patient)

        doublons_trouves, liste_propre = nettoyer_doublons(patients_valides)
        log(f"Nettoyage : {len(liste_propre)} valides, {len(patients_rejetes)} rejetés, {len(doublons_trouves)} doublons")
        return liste_propre, patients_rejetes, doublons_trouves
    except Exception as e:
        log(f"Erreur nettoyage : {e}")
        print(f"Erreur : {e}")
        return [], [], []

#---------------------CHOIX 4 ---------------------------#
def choix4(chemin):
    try:
        patients_valides, patients_rejetes, doublons = choix3(chemin)
        print(f"Total patients lus : {patient_total(patients_valides, patients_rejetes)}")
        print(f"Patients valides : {nombre_valides(patients_valides)}")
        print(f"Doublons supprimés : {len(doublons)}")
        print(f"Lignes rejetées : {len(patients_rejetes)}")
        print(f"Moyenne âge : {moyenne_age(patients_valides):.2f}")
        print(f"Moyenne poids : {moyenne_poids(patients_valides):.2f}")
        print(f"Ville la plus fréquente : {ville_frequente(patients_valides)}")
        print("Répartition groupes sanguins :")
        for groupe, nombre in groupe_sanguin(patients_valides).items():
            print(f"  {groupe} : {nombre} patients")
        log("Statistiques affichées")
    except Exception as e:
        log(f"Erreur statistiques : {e}")
        print(f"Erreur : {e}")

#---------------------CHOIX 5 ---------------------------#
def choix5(chemin):
    try:
        patients_valides, patients_rejetes, doublons = choix3(chemin)
        export_csv(patients_valides, "data/patients_propres.csv")
        export_json(patients_valides, "data/patients_propres.json")
        exporter_rapport(
            patient_total(patients_valides, patients_rejetes),
            nombre_valides(patients_valides),
            len(patients_rejetes),
            len(doublons),
            moyenne_age(patients_valides),
            moyenne_poids(patients_valides),
            ville_frequente(patients_valides),
            groupe_sanguin(patients_valides)
        )
        log("Export CSV, JSON et rapport effectués")
    except Exception as e:
        log(f"Erreur export : {e}")
        print(f"Erreur : {e}")

#---------------------CHOIX 6 ---------------------------#
def choix6(chemin, critere, valeur):
    try:
        patients_valides, patients_rejetes, doublons = choix3(chemin)
        resultats = rechercher_patient(patients_valides, critere, valeur)
        log(f"Recherche '{valeur}' par '{critere}' : {len(resultats)} résultat(s)")
        return resultats
    except Exception as e:
        log(f"Erreur recherche : {e}")
        print(f"Erreur : {e}")
        return []

#---------------------CHOIX 7 ---------------------------#
def choix7():
    print("Au revoir !")
    log("Programme terminé")
    exit()