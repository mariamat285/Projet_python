from datetime import datetime
def log(message):
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"[{horodatage}] {message}\n"
    try:
        with open("logs/logs.txt", "a", encoding="UTF-8") as fichier:
            fichier.write(ligne)
    except Exception as e:
        print(f"Erreur log : {e}")