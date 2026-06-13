#---------------IMPORTATION DES FONCTIONS-----------------------------
from choix import choix1,choix2,choix3,choix4,choix5,choix6,choix7

#--------------------COLORATION MENU -------------------------------------
VIOLET = "\033[95m"
CYAN   = "\033[96m"
VERT   = "\033[92m"
ROUGE  = "\033[91m"
JAUNE  = "\033[93m"
RESET  = "\033[0m"
GRAS   = "\033[1m"

#----------------DEMANDE DE FICHIER-------------------------------------
while True:
    chemin = input("Veuillez entrer le chemin du fichier : ")
    try:
        open(chemin, 'r').close()
        print(f"{VERT}V{RESET} Fichier trouvé !{RESET}")
        break
    except FileNotFoundError:
        print(f"{ROUGE}X{RESET} Fichier introuvable, réessayez.{RESET}")

#-----------------CREATION MENU ----------------------------------------
while True:
    print(f"""
{VIOLET}{GRAS}============================================{RESET}
{CYAN}{GRAS} SYSTÈME DE NETTOYAGE DE DONNÉES MÉDICALES{RESET}
{VIOLET}{GRAS}============================================{RESET}
{JAUNE}1.{RESET} Charger les données brutes
{JAUNE}2.{RESET} Afficher les anomalies détectées
{JAUNE}3.{RESET} Nettoyer les données
{JAUNE}4.{RESET} Afficher les statistiques
{JAUNE}5.{RESET} Exporter les données propres
{JAUNE}6.{RESET} Rechercher un patient
{ROUGE}7.{RESET} Quitter
""")
    choix = input("Choix : ")

    if choix == "1":
        patients, chemin = choix1(chemin)
        if len(patients) > 0:
            print(f"{VERT}V{RESET} {len(patients)} patients chargés.{RESET}")
        else:
            print(f"{ROUGE}X{RESET} Fichier introuvable, réessayez.{RESET}")

    elif choix == "2":
        choix2(chemin)

    elif choix == "3":
        liste_propre, patients_rejetes, doublons_trouves = choix3(chemin)
        print(f"{VERT}V{RESET} Nettoyage terminé ! {len(liste_propre)} valides, {len(patients_rejetes)} rejetés, {len(doublons_trouves)} doublons.{RESET}")

    elif choix == "4":
        choix4(chemin)

    elif choix == "5":
        choix5(chemin)
        print(f"{VERT}V{RESET} Fichiers exportés dans data/{RESET}")

    elif choix == "6":
        print(f"""
{VIOLET}{GRAS}=== RECHERCHE PATIENT ==={RESET}
{JAUNE}Critères :{RESET} id · nom · prenom · age · telephone · ville · groupe_sanguin · poids · taille
""")
        critere = input(f"{CYAN}Critère : {RESET}")
        valeur = input(f"{CYAN}Valeur  : {RESET}")
        resultats = choix6(chemin, critere, valeur)
        if len(resultats) == 0:
            print(f"{ROUGE}X{RESET} Aucun patient trouvé{RESET}")
        else:
            print(f"{VERT}V{RESET} {len(resultats)} patient(s) trouvé(s){RESET}")
            for patient in resultats:
                print(f"""
{VIOLET}{'─'*50}{RESET}
{JAUNE}ID{RESET}            : {patient['id']}
{JAUNE}Nom{RESET}           : {patient['nom']} {patient['prenom']}
{JAUNE}Âge{RESET}           : {patient['age']} ans
{JAUNE}Téléphone{RESET}     : {patient['telephone']}
{JAUNE}Ville{RESET}         : {patient['ville']}
{JAUNE}Groupe sanguin{RESET}: {patient['groupe_sanguin']}
{JAUNE}Poids{RESET}         : {patient['poids']} kg
{JAUNE}Taille{RESET}        : {patient['taille']} cm
{VIOLET}{'─'*50}{RESET}
""")

    elif choix == "7":
        choix7()
        break

    else:
        print(f"{ROUGE}X{RESET} Choix invalide ! Veuillez choisir entre 1 et 7.{RESET}")