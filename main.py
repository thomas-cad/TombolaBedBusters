import pandas as pd

def GetUsers(csv_file: str):
    try:
        df = pd.read_csv(csv_file)
        # Vérifiez si les colonnes nécessaires sont présentes
        required_columns = {"mail"}
        if not required_columns.issubset(df.columns):
            print(f"Le fichier {csv_file} doit contenir les colonnes : {', '.join(required_columns)}")
            return None
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

def tombola(users, lots):
    users_list = users.copy()  # Copie pour éviter de modifier la source
    winners = []

    for lot, quantity in lots.items():
        for _ in range(quantity):
            if not users_list.empty:
                winner = users_list.sample(n=1)
                winners.append([winner.iloc[0]["mail"], lot])
                users_list = users_list.drop(winner.index).reset_index(drop=True)
    
    return winners

# Définir le nombre de lots dans le code
lots = {
    "Lunch Box": 5,
    "Noël Pack": 3,
    "Shampoing": 10,
    "Pack Savon": 7,
    "Parfum": 2,
    "Tee-shirt": 4,
    "Banane": 6,
    "Bob": 111
}

# Calculer le nombre total de lots
total_lots = sum(lots.values())

users = GetUsers("tombola.csv")
if users is None or users.empty:
    print("Aucun utilisateur disponible pour la tombola.")
    exit()

# Decommenter pour tombola 100% gagnante
# Vérifier si le nombre de lignes du CSV est différent du nombre total de lots
if len(users) != total_lots:
    print(f"Le nombre d'utilisateurs ({len(users)}) est différent du nombre total de lots ({total_lots}).")
    exit()

# Effectuer la tombola
winners = tombola(users, lots)

# Exporter les résultats
winners_df = pd.DataFrame(winners, columns=["mail", "lot"])
winners_df.to_csv("gagnants.csv", index=False)

print("La tombola est terminée ! Résultats enregistrés dans 'gagnants.csv'.")