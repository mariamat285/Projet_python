#------------------------EXPORTER FICHIER CSV------------------------------------------------------
def export_csv(patients_valides, fichier):
    try:
        with open(fichier, "w", encoding="UTF-8") as contenu:
            contenu.write("id,nom,prenom,age,telephone,ville,groupe_sanguin,poids,taille\n")
            for patient in patients_valides:
                ligne = f"{patient['id']},{patient['nom']},{patient['prenom']},{patient['age']},{patient['telephone']},{patient['ville']},{patient['groupe_sanguin']},{patient['poids']},{patient['taille']}\n"
                contenu.write(ligne)
    except Exception as e:
        print(f"Erreur export CSV : {e}")
#------------------------EXPORTER FICHIER JSON------------------------------------------------------
import json

def export_json(patients_valides, fichier):
    try:
        with open(fichier, "w", encoding="utf-8") as contenu:
            json.dump(patients_valides, contenu, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erreur export JSON : {e}")

#------------------------CONTENU RAPPORT------------------------------------------------
def exporter_rapport(total, valides, rejetes, doublons, moy_age, moy_poids, ville_freq, groupes_sanguin):
    try:
        with open("rapport/rapport.txt", "w", encoding="UTF-8") as contenu:
            contenu.write("=== RAPPORT DE NETTOYAGE ===\n")
            contenu.write(f"Total patients lus : {total}\n")
            contenu.write(f"Patients valides : {valides}\n")
            contenu.write(f"Doublons supprimés : {doublons}\n")
            contenu.write(f"Lignes rejetées : {rejetes}\n")
            contenu.write(f"Moyenne âge : {moy_age}\n")
            contenu.write(f"Moyenne poids : {moy_poids}\n")
            contenu.write(f"Ville la plus fréquente : {ville_freq}\n")
            contenu.write("Répartition groupes sanguins :\n")
            for groupe, nombre in groupes_sanguin.items():
                contenu.write(f"  {groupe} : {nombre}\n")
    except Exception as e:
        print(f"Erreur export rapport : {e}")